from trilobot.simple_controller import SimpleController


def create_8bitdo_lite_controller():
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


def create_rock_candy_controller():
    controller = SimpleController("Performance Designed Products Rock Candy Wireless Gamepad for PS3")

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


def create_xbox360_wireless_controller(stick_deadzone_percent=0.2):
    controller = SimpleController("Xbox 360 Wireless Receiver")

    # Button and axis registrations for Rock Candy PS3 Controller
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
    controller.register_button("LS", 317)
    controller.register_button("RS", 318)

    controller.register_axis("LX", 0, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("LY", 1, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RX", 3, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RY", 4, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_trigger_axis("LT", 2, 0, 255, alt_name="L2")
    controller.register_trigger_axis("RT", 5, 0, 255, alt_name="R2")
    return controller
