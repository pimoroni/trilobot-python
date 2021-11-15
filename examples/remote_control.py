#!/usr/bin/env python

import time
import math
from colorsys import hsv_to_rgb
from trilobot import Trilobot, controller_mappings

print("Trilobot Remote Control Demo\n")

trilobot = Trilobot()

#
# Uncomment one of the lines below to use one of the existing controller
# # mappings. Or create your own using the SimpleController class
#
# controller = controller_mappings.create_8bitdo_lite_controller()
# controller = controller_mappings.create_8bitdo_sn30_controller()
# controller = controller_mappings.create_rock_candy_controller()
controller = controller_mappings.create_xbox360_wireless_controller()

# Attempt to connect to the created controller
controller.connect()

for led in range(trilobot.NUM_UNDERLIGHTS):
    trilobot.fill_underlighting(0, 0, 0)
    trilobot.set_underlighting(led, 1.0, 0, 0)
    trilobot.show_underlighting()
    time.sleep(0.1)
    trilobot.fill_underlighting(0, 0, 0)
    trilobot.set_underlighting(led, 0, 1.0, 0)
    trilobot.show_underlighting()
    time.sleep(0.1)
    trilobot.fill_underlighting(0, 0, 0)
    trilobot.set_underlighting(led, 0, 0, 1.0)
    trilobot.show_underlighting()
    time.sleep(0.1)

trilobot.fill_underlighting(0, 0, 0)
trilobot.show_underlighting()

h = 0
v = 0
spacing = 1.0 / trilobot.NUM_UNDERLIGHTS

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
        trilobot.disable_motors()

    if controller.is_connected():
        for led in range(trilobot.NUM_UNDERLIGHTS):
            led_h = h + (led * spacing)
            if led_h >= 1.0:
                led_h -= 1.0

            if controller.read_button("A"):
                colour = [0, 1.0, 0]
            else:
                colour = hsv_to_rgb(led_h, 1, 1)
            trilobot.set_underlighting(led, colour[0], colour[1], colour[2])

        trilobot.show_underlighting()
        h += 0.5 / 360
        if h >= 1.0:
            h -= 1.0

        lx = controller.read_axis("LX")
        ly = 0 - controller.read_axis("LY")
        trilobot.set_left_speed(ly + lx)
        trilobot.set_right_speed(ly - lx)
    else:
        val = (math.sin(v) / 2.0) + 0.5
        trilobot.fill_underlighting(val * 0.5, 0, 0)
        trilobot.show_underlighting()
        v += math.pi / 200

    if trilobot.read_button(trilobot.BUTTON_A):
        print("A pressed")
        a = min(a + 0.01, 1.0)
    else:
        a = max(a - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_A, a)

    if trilobot.read_button(trilobot.BUTTON_B):
        b = min(b + 0.01, 1.0)
        print("B pressed")
    else:
        b = max(b - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_B, b)

    if trilobot.read_button(trilobot.BUTTON_X):
        x = min(x + 0.01, 1.0)
        print("X pressed")
    else:
        x = max(x - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_X, x)

    if trilobot.read_button(trilobot.BUTTON_Y):
        y = min(y + 0.01, 1.0)
        print("Y pressed")
    else:
        y = max(y - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_Y, y)

    time.sleep(0.01)
