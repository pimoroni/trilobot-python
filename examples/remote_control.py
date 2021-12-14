#!/usr/bin/env python3

import time
import math
from trilobot import *
from trilobot import controller_mappings

"""
An advanced example of how Trilobot can be remote controlled using a controller or gamepad.
This will require one of the supported controllers to already be paired to your Trilobot.

At startup a list of supported controllers will be shown, with you being asked to select one.
The program will then attempt to connect to the controller, and if successful Trilobot's
underlights will illuminate with a rainbow pattern.

From there you can drive your Trilobot around using the left analog stick or d-pad.
Pressing the right trigger will switch to Tank-steer mode, where the left analog stick
controls the left wheel, and the right analog stick controls the right wheel.
Pressing the left trigger will switch back to regular mode.

If your controller becomes disconnected Trilobot will stop moving and show a slow red
pulsing animation on its underlights. Simply reconnect your controller and after 10 to 20
seconds, the program should find your controller again and start up again.

Support for further controllers can be added to library/trilobot/controller_mappings.py

Press CTRL + C to exit.
"""
print("Trilobot Example: Remote Control\n")


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tbot = Trilobot()

# Presents the user with an option of what controller to use
controller = controller_mappings.choose_controller()

# Attempt to connect to the created controller
controller.connect()

# Run an amination on the underlights to show a controller has been selected
for led in range(NUM_UNDERLIGHTS):
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, RED)
    time.sleep(0.1)
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, GREEN)
    time.sleep(0.1)
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, BLUE)
    time.sleep(0.1)

tbot.clear_underlighting()

h = 0
v = 0
spacing = 1.0 / NUM_UNDERLIGHTS

tank_steer = False
while True:

    if not controller.is_connected():
        # Attempt to reconnect to the controller if 10 seconds have passed since the last attempt
        controller.reconnect(10, True)

    try:
        # Get the latest information from the controller. This will throw a RuntimeError if the controller connection is lost
        controller.update()
    except RuntimeError:
        # Lost contact with the controller, so disable the motors to stop Trilobot if it was moving
        tbot.disable_motors()

    if controller.is_connected():

        # Read the controller bumpers to see if the tank steer mode has been enabled or disabled
        try:
            if controller.read_button("L1") and tank_steer:
                tank_steer = False
                print("Tank Steering Disabled")
            if controller.read_button("R1") and not tank_steer:
                tank_steer = True
                print("Tank Steering Enabled")
        except ValueError:
            # Cannot find 'L1' or 'R1' on this controller
            print("Tank Steering Not Available")

        try:
            if tank_steer:
                # Have the left stick's Y axis control the left motor, and the right stick's Y axis control the right motor
                ly = controller.read_axis("LY")
                ry = controller.read_axis("RY")
                tbot.set_left_speed(-ly)
                tbot.set_right_speed(-ry)
            else:
                # Have the left stick control both motors
                lx = controller.read_axis("LX")
                ly = 0 - controller.read_axis("LY")
                tbot.set_left_speed(ly + lx)
                tbot.set_right_speed(ly - lx)
        except ValueError:
            # Cannot find 'LX', 'LY', or 'RY' on this controller
            tbot.disable_motors()

        # Run a rotating rainbow effect on the RGB underlights
        for led in range(NUM_UNDERLIGHTS):
            led_h = h + (led * spacing)
            if led_h >= 1.0:
                led_h -= 1.0

            try:
                if controller.read_button("A"):
                    tbot.set_underlight_hsv(led, 0.0, 0.0, 0.7, show=False)
                else:
                    tbot.set_underlight_hsv(led, led_h, show=False)
            except ValueError:
                # Cannot find 'A' on this controller
                tbot.set_underlight_hsv(led, led_h, show=False)

        tbot.show_underlighting()

        # Advance the rotating rainbow effect
        h += 0.5 / 360
        if h >= 1.0:
            h -= 1.0

    else:
        # Run a slow red pulsing animation to show there is no controller connected
        val = (math.sin(v) / 2.0) + 0.5
        tbot.fill_underlighting(val * 127, 0, 0)
        v += math.pi / 200

    time.sleep(0.01)
