import time
from evdev import InputDevice, ecodes, list_devices


# Maps a value from one range to another
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Button():
    def __init__(self, name, alt_name, ev_code, ev_type, pressed_value, released_value, pressed_callback, released_callback):
        self.name = name
        self.alt_name = alt_name
        self.ev_code = ev_code
        self.ev_type = ev_type
        self.pressed_value = pressed_value
        self.released_value = released_value
        self.pressed_callback = pressed_callback
        self.released_callback = released_callback
        self.pressed = False

    def assign_callbacks(self, pressed_callback, released_callback):
        self.pressed_callback = pressed_callback
        self.released_callback = pressed_callback

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
    def __init__(self, name, alt_name, ev_code, min_value, max_value, min_output, max_output, deadzone_percent, changed_callback):
        self.name = name
        self.alt_name = alt_name
        self.ev_code = ev_code
        self.min_value = min_value
        self.max_value = max_value
        self.min_output = min_output
        self.max_output = max_output
        self.deadzone_percent = deadzone_percent
        self.changed_callback = changed_callback
        self.percent = 0.0

    def assign_callback(self, changed_callback):
        self.changed_callback = changed_callback

    def reset(self):
        self.percent = 0.0

    def set_percent(self, percent):
        self.percent = percent
        if self.changed_callback:
            self.changed_callback(self.percent)

    def get_percent(self):
        if self.percent < 0.0 - self.deadzone_percent or self.percent > 0.0 + self.deadzone_percent:
            return self.percent
        else:
            return 0.0

    def is_this(self, ev_code, ev_type):
        return (ev_code == self.ev_code and ev_type == ecodes.EV_ABS)


class SimpleController():
    def __init__(self, controller_name):
        """Initialise SimpleController
        """
        self.controller_to_find = controller_name

        self.controller = None
        self.last_attempt_time = 0

        self.buttons = []
        self.axes = []

    def register_button(self, name, ev_code, pressed_callback=None, released_callback=None, alt_name=None):
        for button in self.buttons:
            if name == button.name:
                raise ValueError("A button with the name '" + name + "' is already registered. Use a different name")
            if name == button.alt_name:
                raise ValueError("A button with the alt_name '" + name + "' is already registered. Use a different name")
            if alt_name:
                if alt_name == button.name:
                    raise ValueError("A button with the name '" + name + "' is already registered. Use a different alt_name")
                if alt_name == button.alt_name:
                    raise ValueError("A button with the alt_name '" + name + "' is already registered. Use a different alt_name")
        self.buttons.append(Button(name, alt_name, ev_code, ecodes.EV_KEY, 1, 0, pressed_callback, released_callback))

    def register_axis_as_button(self, name, ev_code, pressed_value=1, released_value=0, pressed_callback=None, released_callback=None, alt_name=None):
        for button in self.buttons:
            if name == button.name:
                raise ValueError("A button with the name '" + name + "' is already registered. Use a different name")
            if name == button.alt_name:
                raise ValueError("A button with the alt_name '" + name + "' is already registered. Use a different name")
            if alt_name:
                if alt_name == button.name:
                    raise ValueError("A button with the name '" + name + "' is already registered. Use a different alt_name")
                if alt_name == button.alt_name:
                    raise ValueError("A button with the alt_name '" + name + "' is already registered. Use a different alt_name")
        self.buttons.append(Button(name, ev_code, alt_name, ecodes.EV_ABS, pressed_value, released_value, pressed_callback, released_callback))

    def register_axis(self, name, ev_code, min_value=-1, max_value=1, deadzone_percent=0.0, changed_callback=None, alt_name=None):
        for axis in self.axes:
            if name == axis.name:
                raise ValueError("An axis with the name '" + name + "' is already registered. Use a different name")
            if name == axis.alt_name:
                raise ValueError("An axis with the alt_name '" + name + "' is already registered. Use a different name")
            if alt_name:
                if alt_name == axis.name:
                    raise ValueError("An axis with the name '" + name + "' is already registered. Use a different alt_name")
                if alt_name == axis.alt_name:
                    raise ValueError("An axis with the alt_name '" + name + "' is already registered. Use a different alt_name")
        self.axes.append(Axis(name, alt_name, ev_code, min_value, max_value, -1.0, 1.0, deadzone_percent, changed_callback))

    def register_trigger_axis(self, name, ev_code, min_value=0, max_value=1, deadzone_percent=0.0, changed_callback=None, alt_name=None):
        for axis in self.axes:
            if name == axis.name:
                raise ValueError("An axis with the name '" + name + "' is already registered. Use a different name")
            if name == axis.alt_name:
                raise ValueError("An axis with the alt_name '" + name + "' is already registered. Use a different name")
            if alt_name:
                if alt_name == axis.name:
                    raise ValueError("An axis with the name '" + name + "' is already registered. Use a different alt_name")
                if alt_name == axis.alt_name:
                    raise ValueError("An axis with the alt_name '" + name + "' is already registered. Use a different alt_name")
        self.axes.append(Axis(name, alt_name, ev_code, min_value, max_value, 0.0, 1.0, deadzone_percent, changed_callback))

    def assign_button_callbacks(self, name, pressed_callback, released_callback):
        button_found = False
        for button in self.buttons:
            if name == button.name or name == button.alt_name:
                button.assign_callbacks(pressed_callback, released_callback)
                button_found = True
                break

        if not button_found:
            raise ValueError("A button with the name or alt_name'" + name + "' could not be found")

    def assign_axis_callback(self, name, changed_callback):
        axis_found = False
        for axis in self.axes:
            if name == axis.name or name == axis.alt_name:
                axis.assign_callback(changed_callback)
                axis_found = True
                break

        if not axis_found:
            raise ValueError("An axis with the name or alt_name'" + name + "' could not be found")

    def is_connected(self):
        return self.controller is not None

    def connect(self, debug=True):
        if debug:
            print("Searching for '", self.controller_to_find, "'... ", sep="", end="")

        self.controller = None
        devices = [InputDevice(path) for path in list_devices()]
        for device in devices:
            if self.controller_to_find in device.name:
                self.controller = device
                break

        if debug:
            if self.controller:
                if self.controller_to_find == self.controller.name:
                    print("connected")
                else:
                    print("connected to '", self.controller.name, "'", sep="")
            else:
                print("not found")

    def reconnect(self, time_between_attempts=0, debug=True):
        if self.controller is None:
            currenttime = time.time()
            if currenttime - self.last_attempt_time >= time_between_attempts:
                if debug:
                    print("Attempting to reconnect to '", self.controller_to_find, "'... ", sep="", end="")
                self.connect(False)
                self.last_attempt_time = currenttime
                if debug:
                    if self.controller:
                        if self.controller_to_find == self.controller.name:
                            print("reconnected")
                        else:
                            print("reconnected to '", self.controller.name, "'", sep="")
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
            print("Disconnected from '", self.controller_to_find, "'", sep="")

    def read_button(self, name):
        for button in self.buttons:
            if name == button.name or name == button.alt_name:
                return button.is_pressed()
        raise ValueError("Cannot find button '" + name + "'")

    def read_axis(self, name):
        for axis in self.axes:
            if name == axis.name or name == axis.alt_name:
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
                            percent = map(event.value, axis.min_value, axis.max_value, axis.min_output, axis.max_output)

                            if percent > 0.0 - axis.deadzone_percent and percent < 0.0 + axis.deadzone_percent:
                                percent = 0.0
                                if debug:
                                    print("'", axis.name, "' changed to 0.000 (within deadzone)", sep="")
                            else:
                                if debug:
                                    print("'", axis.name, "' changed to {:.3f}".format(percent), sep="")
                            axis.set_percent(percent)

                    event = self.controller.read_one()
            except OSError:
                self.disconnect(False)
                if debug:
                    print("Connection to '", self.controller_to_find, "' lost", sep="")
                raise RuntimeError()
