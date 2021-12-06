#!/usr/bin/env python3

import time
import math
from trilobot import *
from trilobot import controller_mappings

"""
TODO
"""
print("Trilobot Example: Remote Control\n")


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tbot = Trilobot()

#
# Uncomment one of the lines below to use one of the existing controller
# mappings. Or create your own using the SimpleController class
#
# controller = controller_mappings.create_8bitdo_lite_controller()
# controller = controller_mappings.create_8bitdo_sn30_controller()
# controller = controller_mappings.create_8bitdo_sn30_pro_controller()
# controller = controller_mappings.create_rock_candy_controller()
# controller = controller_mappings.create_ps4_wireless_controller()
# controller = controller_mappings.create_ps4_wireless_controller_touchpad()
# controller = controller_mappings.create_ps4_wireless_controller_motion()
# controller = controller_mappings.create_xbox360_wireless_controller()

controller = controller_mappings.choose_controller()

# Attempt to connect to the created controller
controller.connect()

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

a = 0
b = 0
x = 0
y = 0
while True:

    if not controller.is_connected():
        # Attempt to reconnect to the controller if 10 seconds have passed since the last attempt
        controller.reconnect(10, True)

    try:
        controller.update()
    except RuntimeError:
        tbot.disable_motors()

    if controller.is_connected():
        for led in range(NUM_UNDERLIGHTS):
            led_h = h + (led * spacing)
            if led_h >= 1.0:
                led_h -= 1.0

            try:
                if controller.read_button("L1") and tank_steer:
                    tank_steer = False
                    print("Tank Steering Disabled")
                if controller.read_button("R1") and not tank_steer:
                    tank_steer = True
                    print("Tank Steering Enabled")
            except ValueError:  # Cannot find 'L1' or 'R1'
                print("Tank Steering Not Available")

            try:
                if controller.read_button("A"):
                    tbot.set_underlight_hsv(led, 0.0, 0.0, 0.7, show=False)
                else:
                    tbot.set_underlight_hsv(led, led_h, show=False)
            except ValueError:  # Cannot find 'A'
                tbot.set_underlight_hsv(led, led_h, show=False)

        tbot.show_underlighting()
        h += 0.5 / 360
        if h >= 1.0:
            h -= 1.0

        if tank_steer:
            ly = controller.read_axis("LY")
            ry = controller.read_axis("RY")
            tbot.set_left_speed(-ly)
            tbot.set_right_speed(-ry)
        else:
            lx = controller.read_axis("LX")
            ly = 0 - controller.read_axis("LY")
            tbot.set_left_speed(ly + lx)
            tbot.set_right_speed(ly - lx)

    else:
        val = (math.sin(v) / 2.0) + 0.5
        tbot.fill_underlighting(val * 127, 0, 0)
        v += math.pi / 200

    if tbot.read_button(BUTTON_A):
        print("A pressed")
        a = min(a + 0.01, 1.0)
    else:
        a = max(a - 0.01, 0.0)
    tbot.set_button_led(BUTTON_A, a)

    if tbot.read_button(BUTTON_B):
        b = min(b + 0.01, 1.0)
        print("B pressed")
    else:
        b = max(b - 0.01, 0.0)
    tbot.set_button_led(BUTTON_B, b)

    if tbot.read_button(BUTTON_X):
        x = min(x + 0.01, 1.0)
        print("X pressed")
    else:
        x = max(x - 0.01, 0.0)
    tbot.set_button_led(BUTTON_X, x)

    if tbot.read_button(BUTTON_Y):
        y = min(y + 0.01, 1.0)
        print("Y pressed")
    else:
        y = max(y - 0.01, 0.0)
    tbot.set_button_led(BUTTON_Y, y)

    time.sleep(0.01)
