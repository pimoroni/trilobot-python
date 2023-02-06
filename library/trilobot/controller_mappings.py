from trilobot.simple_controller import SimpleController


def create_8bitdo_lite_controller():
    """ Create a controller class for the 8BitDo Lite controller.
    """
    controller = SimpleController("8BitDo Lite gamepad")

    # Button and axis registrations for 8BitDo Lite
    controller.register_button("A", 305)
    controller.register_button("B", 304)
    controller.register_button("X", 307)
    controller.register_button("Y", 306)
    controller.register_button("Plus", 311, alt_name="Start")
    controller.register_button("Minus", 310, alt_name="Select")
    controller.register_button("L1", 308, alt_name="LB")
    controller.register_axis_as_button("L2", 2, 0, 1023, alt_name="LT")
    controller.register_button("R1", 309, alt_name="RB")
    controller.register_axis_as_button("R2", 5, 0, 1023, alt_name="RT")
    controller.register_button("Home", 139)
    controller.register_axis_as_button("L_Left", 0, 0, 32768)
    controller.register_axis_as_button("L_Right", 0, 65535, 32768)
    controller.register_axis_as_button("L_Up", 1, 0, 32768)
    controller.register_axis_as_button("L_Down", 1, 65535, 32768)
    controller.register_axis_as_button("R_Left", 3, 0, 32768)
    controller.register_axis_as_button("R_Right", 3, 65535, 32768)
    controller.register_axis_as_button("R_Up", 4, 0, 32768)
    controller.register_axis_as_button("R_Down", 4, 65535, 32768)
    controller.register_axis_as_button("Left", 16, -1, 0)
    controller.register_axis_as_button("Right", 16, 1, 0)
    controller.register_axis_as_button("Up", 17, -1, 0)
    controller.register_axis_as_button("Down", 17, 1, 0)

    controller.register_axis("LX", 0, 0, 65536)
    controller.register_axis("LY", 1, 0, 65536)
    controller.register_axis("RX", 3, 0, 65536)
    controller.register_axis("RY", 4, 0, 65536)
    return controller


def create_8bitdo_sn30_controller():
    """ Create a controller class for the 8BitDo SN30 controller.
    """
    controller = SimpleController("8Bitdo SN30 GamePad")

    # Button and axis registrations for 8BitDo SN30
    controller.register_button("A", 304)
    controller.register_button("B", 305)
    controller.register_button("X", 307)
    controller.register_button("Y", 308)
    controller.register_button("Start", 315)
    controller.register_button("Select", 314)
    controller.register_button("L1", 310, alt_name="LB")
    controller.register_button("R1", 311, alt_name="RB")
    controller.register_axis_as_button("Left", 0, 0, 127)
    controller.register_axis_as_button("Right", 0, 255, 127)
    controller.register_axis_as_button("Up", 1, 0, 127)
    controller.register_axis_as_button("Down", 1, 255, 127)

    controller.register_axis("LX", 0, 0, 256)
    controller.register_axis("LY", 1, 0, 256)
    return controller


def create_8bitdo_sn30_pro_controller():
    """ Create a controller class for the 8BitDo SN30 Pro+ controller.
    """
    controller = SimpleController("8BitDo SN30 Pro+")

    # Button and axis registrations for 8BitDo SN30 Pro+
    controller.register_button("A", 305, alt_name="Cross")
    controller.register_button("B", 304, alt_name="Circle")
    controller.register_button("X", 307, alt_name="Square")
    controller.register_button("Y", 306, alt_name="Triangle")
    controller.register_button("Plus", 311, alt_name="Start")
    controller.register_button("Minus", 310, alt_name="Select")
    controller.register_button("L1", 308, alt_name="LB")
    controller.register_axis_as_button("L2", 2, 0, 1023, alt_name="LT")
    controller.register_button("R1", 309, alt_name="RB")
    controller.register_axis_as_button("R2", 5, 0, 1023, alt_name="RT")
    controller.register_button("Home", 139)
    controller.register_axis_as_button("L_Left", 0, 0, 32768)
    controller.register_axis_as_button("L_Right", 0, 65535, 32768)
    controller.register_axis_as_button("L_Up", 1, 0, 32768)
    controller.register_axis_as_button("L_Down", 1, 65535, 32768)
    controller.register_axis_as_button("R_Left", 3, 0, 32768)
    controller.register_axis_as_button("R_Right", 3, 65535, 32768)
    controller.register_axis_as_button("R_Up", 4, 0, 32768)
    controller.register_axis_as_button("R_Down", 4, 65535, 32768)
    controller.register_axis_as_button("Left", 16, -1, 0)
    controller.register_axis_as_button("Right", 16, 1, 0)
    controller.register_axis_as_button("Up", 17, -1, 0)
    controller.register_axis_as_button("Down", 17, 1, 0)

    controller.register_axis("LX", 0, 0, 65536)
    controller.register_axis("LY", 1, 0, 65536)
    controller.register_axis("RX", 3, 0, 65536)
    controller.register_axis("RY", 4, 0, 65536)
    return controller


def create_rock_candy_controller():
    """ Create a controller class for the RockCandy PS3 controller.
    """
    controller = SimpleController("Performance Designed Products")

    # Button and axis registrations for Rock Candy PS3 Controller
    controller.register_button("Cross", 305, alt_name="A")
    controller.register_button("Circle", 306, alt_name="B")
    controller.register_button("Square", 304, alt_name="X")
    controller.register_button("Triangle", 307, alt_name="Y")
    controller.register_button("Start", 313)
    controller.register_button("Select", 312)
    controller.register_button("Home", 316)
    controller.register_button("L1", 308, alt_name="LB")
    controller.register_button("L2", 310, alt_name="LT")
    controller.register_button("R1", 309, alt_name="RB")
    controller.register_button("R2", 311, alt_name="RT")
    controller.register_axis_as_button("Left", 16, -1, 0)
    controller.register_axis_as_button("Right", 16, 1, 0)
    controller.register_axis_as_button("Up", 17, -1, 0)
    controller.register_axis_as_button("Down", 17, 1, 0)

    controller.register_axis("LX", 0, 0, 256)
    controller.register_axis("LY", 1, 0, 256)
    controller.register_axis("RX", 2, 0, 256)
    controller.register_axis("RY", 5, 0, 256)
    return controller


def create_xbox_360_wireless_controller(stick_deadzone_percent=0.2):
    """ Create a controller class for the Xbox 360 Wireless controller.
    stick_deadzone_percent: the deadzone amount to apply to the controller's analog sticks
    """
    controller = SimpleController("Xbox 360 Wireless Receiver")

    # Button and axis registrations for Xbox 360 Wireless Controller
    controller.register_button("A", 304, alt_name="Cross")
    controller.register_button("B", 305, alt_name="Circle")
    controller.register_button("X", 307, alt_name="Square")
    controller.register_button("Y", 308, alt_name="Triangle")
    controller.register_button("Start", 315)
    controller.register_button("Select", 314)
    controller.register_button("Home", 316)
    controller.register_button("LB", 310, alt_name="L1")
    controller.register_axis_as_button("LT", 2, 255, 0, alt_name="L2")
    controller.register_button("RB", 311, alt_name="R1")
    controller.register_axis_as_button("RT", 5, 255, 0, alt_name="R2")
    controller.register_button("Left", 704)
    controller.register_button("Right", 705)
    controller.register_button("Up", 706)
    controller.register_button("Down", 707)
    controller.register_button("LS", 317, alt_name="L3")
    controller.register_button("RS", 318, alt_name="R3")

    controller.register_axis("LX", 0, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("LY", 1, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RX", 3, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RY", 4, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_trigger_axis("LT", 2, 0, 255, alt_name="L2")
    controller.register_trigger_axis("RT", 5, 0, 255, alt_name="R2")
    return controller


def create_xbox_one_wireless_controller(stick_deadzone_percent=0.2):
    """ Create a controller class for the Xbox One Wireless controller.
    stick_deadzone_percent: the deadzone amount to apply to the controller's analog sticks
    """
    controller = SimpleController("Xbox Wireless Controller")

    # Button and axis registrations for Xbox One Wireless Controller
    controller.register_button("A", 304, alt_name="Cross")
    controller.register_button("B", 305, alt_name="Circle")
    controller.register_button("X", 307, alt_name="Square")
    controller.register_button("Y", 308, alt_name="Triangle")
    controller.register_button("Start", 315)
    controller.register_button("Select", 314)
    controller.register_button("Home", 316)
    controller.register_button("LB", 310, alt_name="L1")
    controller.register_axis_as_button("LT", 3, 255, 0, alt_name="L2")
    controller.register_button("RB", 311, alt_name="R1")
    controller.register_axis_as_button("RT", 4, 255, 0, alt_name="R2")
    controller.register_button("Left", 704)
    controller.register_button("Right", 705)
    controller.register_button("Up", 706)
    controller.register_button("Down", 707)
    controller.register_button("LS", 317, alt_name="L3")
    controller.register_button("RS", 318, alt_name="R3")

    controller.register_axis("LX", 0, 0, 65535, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("LY", 1, 0, 65535, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RX", 2, 0, 65535, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RY", 5, 0, 65535, deadzone_percent=stick_deadzone_percent)
    controller.register_trigger_axis("LT", 3, 0, 255, alt_name="L2")
    controller.register_trigger_axis("RT", 4, 0, 255, alt_name="R2")
    return controller


def create_ps4_wireless_controller(stick_deadzone_percent=0.1):
    """ Create a controller class for the PlayStation 4 Wireless controller.
    stick_deadzone_percent: the deadzone amount to apply to the controller's analog sticks
    """
    controller = SimpleController("Wireless Controller", exact_match=True)

    # Button and axis registrations for PS4 Controller
    controller.register_button("Cross", 304, alt_name="A")
    controller.register_button("Circle", 305, alt_name="B")
    controller.register_button("Square", 308, alt_name="X")
    controller.register_button("Triangle", 307, alt_name="Y")
    controller.register_button("Options", 315, alt_name='Start')
    controller.register_button("Share", 314, alt_name='Select')
    controller.register_button("PS", 316, alt_name='Home')
    controller.register_button("L1", 310, alt_name="LB")
    controller.register_button("L2", 312, alt_name="LT")
    controller.register_button("R1", 311, alt_name="RB")
    controller.register_button("R2", 313, alt_name="RT")
    controller.register_axis_as_button("Left", 16, -1, 0)
    controller.register_axis_as_button("Right", 16, 1, 0)
    controller.register_axis_as_button("Up", 17, -1, 0)
    controller.register_axis_as_button("Down", 17, 1, 0)
    controller.register_button("L3", 317, alt_name='LS')
    controller.register_button("R3", 318, alt_name='RS')

    controller.register_axis("LX", 0, 0, 255, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("LY", 1, 0, 255, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RX", 3, 0, 255, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RY", 4, 0, 255, deadzone_percent=stick_deadzone_percent)
    controller.register_trigger_axis("L2", 2, 0, 255, alt_name="LT")
    controller.register_trigger_axis("R2", 5, 0, 255, alt_name="RT")
    return controller


def create_ps4_wireless_controller_touchpad():
    """ Create a controller class for the PlayStation 4 Wireless controller's touchpad.
    """
    controller = SimpleController("Wireless Controller Touchpad", exact_match=True)

    # Button and axis registrations for PS4 Controller Touchpad
    controller.register_button("Touch", 330)
    controller.register_button("Finger", 325)
    controller.register_button("Doubletap", 333)
    controller.register_button("Click", 272, alt_name="A")

    controller.register_axis("X", 0, 0, 1920, alt_name="LX")
    controller.register_axis("Y", 1, 0, 942, alt_name="LY")

    # Currently unhandled codes
    # EV_ABS 57 Tracking ID
    # EV_ABS 53 Position X
    # EV_ABS 54 Position Y
    # EV_ABS 47 Slot
    return controller


def create_ps4_wireless_controller_motion():
    """ Create a controller class for the PlayStation 4 Wireless controller's motion sensors.
    """
    controller = SimpleController("Wireless Controller Motion Sensors", exact_match=True)

    # Button and axis registrations for PS4 Controller Motion
    controller.register_axis("X", 0, 8500, -8500, alt_name="LX")
    controller.register_axis("Y", 1, 8500, -8500, alt_name="LY")
    controller.register_axis("Z", 2, -8500, 8500)
    controller.register_axis("RX", 3, -8500, 8500)
    controller.register_axis("RY", 4, -8500, 8500)
    controller.register_axis("RZ", 5, -8500, 8500)

    return controller


def choose_controller():
    """ Present the user with a selection menu for pre-configured controllers.
    """
    controller_list = [("8BitDo Lite", create_8bitdo_lite_controller),
                       ("8Bitdo SN30", create_8bitdo_sn30_controller),
                       ("8BitDo SN30 Pro+", create_8bitdo_sn30_pro_controller),
                       ("RockCandy Controller", create_rock_candy_controller),
                       ("Xbox 360 Wireless Receiver", create_xbox_360_wireless_controller),
                       ("Xbox One Wireless Receiver", create_xbox_one_wireless_controller),
                       ("PS4 Controller", create_ps4_wireless_controller),
                       ("PS4 Controller - Touchpad", create_ps4_wireless_controller_touchpad),
                       ("PS4 Controller - Motion Sensors", create_ps4_wireless_controller_motion)]

    print("Currently supported controllers:")
    for i in range(0, len(controller_list)):
        print("  ", i, ") ", controller_list[i][0], sep="")

    try:
        controller_id = int(input("Select controller: "))
        if controller_id < 0 or controller_id >= len(controller_list):
            print("Not a valid controller. Exiting")
            quit()

        print("Selected:", controller_list[controller_id][0], end="\n\n")
        return controller_list[controller_id][1]()
    except ValueError:
        print("Not a number. Exiting")
        quit()
