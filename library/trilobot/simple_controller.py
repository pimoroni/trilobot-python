import time
from evdev import InputDevice, ecodes, list_devices


# Maps a value from one range to another
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Button():
    def __init__(self, name, ev_code, ev_type, pressed_value, released_value, pressed_callback, released_callback):
        self.name = name
        self.ev_code = ev_code
        self.ev_type = ev_type
        self.pressed_value = pressed_value
        self.released_value = released_value
        self.pressed_callback = pressed_callback
        self.released_callback = released_callback
        self.pressed = False

    def reset(self):
        self.pressed = False

    def set_pressed(self):
        self.pressed = True
        if self.pressed_callback:
            self.pressed_callback()

    def clear_pressed(self):
        self.pressed = False
        if self.released_callback:
            self.released_callback()

    def is_pressed(self):
        return self.pressed

    def is_this(self, ev_code, ev_type):
        return (ev_code == self.ev_code and ev_type == self.ev_type)


class Axis():
    def __init__(self, name, ev_code, min_value, max_value, changed_callback):
        self.name = name
        self.ev_code = ev_code
        self.min_value = min_value
        self.max_value = max_value
        self.changed_callback = changed_callback
        self.percent = 0.0

    def reset(self):
        self.percent = 0.0

    def set_percent(self, percent):
        self.percent = percent
        if self.changed_callback:
            self.changed_callback(self.percent)

    def get_percent(self):
        return self.percent

    def is_this(self, ev_code, ev_type):
        return (ev_code == self.ev_code and ev_type == ecodes.EV_ABS)


class SimpleController():
    def __init__(self, controller_name):
        """Initialise SimpleController
        """
        self.controller_name = controller_name

        self.controller = None
        self.last_attempt_time = 0

        self.buttons = []
        self.axes = []

    def register_button(self, name, ev_code, pressed_callback=None, released_callback=None):
        for button in self.buttons:
            if name == button.name:
                raise ValueError("A button with the name '" + name + "' is already registered. Use a different name")
        self.buttons.append(Button(name, ev_code, ecodes.EV_KEY, 1, 0, pressed_callback, released_callback))

    def register_axis_as_button(self, name, ev_code, pressed_value=1, released_value=0, pressed_callback=None, released_callback=None):
        for button in self.buttons:
            if name == button.name:
                raise ValueError("A button with the name '" + name + "' is already registered. Use a different name")
        self.buttons.append(Button(name, ev_code, ecodes.EV_ABS, pressed_value, released_value, pressed_callback, released_callback))

    def register_axis(self, name, ev_code, min_value=-1, max_value=1, changed_callback=None):
        for axis in self.axes:
            if name == axis.name:
                raise ValueError("An axis with the name '" + name + "' is already registered. Use a different name")
        self.axes.append(Axis(name, ev_code, min_value, max_value, changed_callback))

    def is_connected(self):
        return self.controller is not None

    def connect(self, debug=True):
        if debug:
            print("Searching for '", self.controller_name, "'... ", sep="", end="")

        self.controller = None
        devices = [InputDevice(path) for path in list_devices()]
        for device in devices:
            if device.name == self.controller_name:
                self.controller = device
                break

        if debug:
            if self.controller:
                print("connected")
            else:
                print("not found")

    def reconnect(self, time_between_attempts=0, debug=True):
        if self.controller is None:
            currenttime = time.time()
            if currenttime - self.last_attempt_time >= time_between_attempts:
                if debug:
                    print("Attempting to reconnect to '", self.controller_name, "'... ", sep="", end="")
                self.connect(False)
                self.last_attempt_time = currenttime
                if debug:
                    if self.controller:
                        print("reconnected")
                    else:
                        print("not found")

    def disconnect(self, debug=True):
        self.controller = None
        self.last_attempt_time = time.time()
        for button in self.buttons:
            button.reset()
        for axis in self.axes:
            axis.reset()
        if debug:
            print("Disconnected from '", self.controller_name, "'", sep="")

    def read_button(self, name):
        for button in self.buttons:
            if name == button.name:
                return button.is_pressed()
        raise ValueError("Cannot find button '" + name + "'")

    def read_axis(self, name):
        for axis in self.axes:
            if name == axis.name:
                return axis.get_percent()
        raise ValueError("Cannot find axis '" + name + "'")

    def update(self, debug=True):
        if self.controller:
            try:
                event = self.controller.read_one()
                while event is not None:
                    for button in self.buttons:
                        if button.is_this(event.code, event.type):
                            if event.value == button.pressed_value:
                                if debug:
                                    print("'", button.name, "' pressed", sep="")
                                button.set_pressed()
                            elif event.value == button.released_value:
                                if debug:
                                    print("'", button.name, "' released", sep="")
                                button.clear_pressed()

                    for axis in self.axes:
                        if axis.is_this(event.code, event.type):
                            percent = map(event.value, axis.min_value, axis.max_value, -1.0, 1.0)
                            if debug:
                                print("'", axis.name, "' changed to ", percent, sep="")
                            axis.set_percent(percent)

                    event = self.controller.read_one()
            except OSError:
                self.disconnect(False)
                if debug:
                    print("Connection to '", self.controller_name, "' lost", sep="")
                raise RuntimeError()
