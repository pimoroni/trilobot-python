#!/usr/bin/env python

import time
import math
from colorsys import hsv_to_rgb
from trilobot import Trilobot
from trilobot.simple_controller import SimpleController

print("Trilobot Remote Control Demo\n")

trilobot = Trilobot()


def set_left_motor(value):
    trilobot.set_motor_speed(0, -value)


def set_right_motor(value):
    trilobot.set_motor_speed(1, value)


controller = SimpleController("8BitDo Lite gamepad")
controller.connect()

# Button and axis registrations for 8BitDo Lite
controller.register_button("A", 305)
controller.register_button("B", 304)
controller.register_button("X", 307)
controller.register_button("Y", 306)
controller.register_button("Plus", 311)
controller.register_button("Minus", 310)
controller.register_button("R1", 309)
controller.register_axis_as_button("R2", 5, 0, 1023)
controller.register_button("L1", 308)
controller.register_axis_as_button("L2", 2, 0, 1023)
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
controller.register_axis("LY", 1, 0, 65536, set_left_motor)
controller.register_axis("RX", 3, 0, 65536)
controller.register_axis("RY", 4, 0, 65536, set_right_motor)
"""
controller = SimpleController("8Bitdo SN30 GamePad")
controller.connect()

# Button and axis registrations for 8BitDo SN30
controller.register_button("A", 304)
controller.register_button("B", 305)
controller.register_button("X", 307)
controller.register_button("Y", 308)
controller.register_button("Start", 315)
controller.register_button("Select", 314)
controller.register_button("R", 311)
controller.register_button("L", 310)
controller.register_axis_as_button("Left", 0, 0, 127)
controller.register_axis_as_button("Right", 0, 255, 127)
controller.register_axis_as_button("Up", 1, 0, 127)
controller.register_axis_as_button("Down", 1, 255, 127)

controller.register_axis("X", 0, -1, 255, set_left_motor)
controller.register_axis("Y", 1, -1, 255, set_right_motor)
"""

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
    else:
        val = (math.sin(v) / 2.0) + 0.5
        trilobot.fill_underlighting(val * 0.5, 0, 0)
        trilobot.show_underlighting()
        v += math.pi / 200

    if trilobot.read_button(trilobot.BUTTON_A):
        a = min(a + 0.01, 1.0)
    else:
        a = max(a - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_A, a)

    if trilobot.read_button(trilobot.BUTTON_B):
        b = min(b + 0.01, 1.0)
    else:
        b = max(b - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_B, b)

    if trilobot.read_button(trilobot.BUTTON_X):
        x = min(x + 0.01, 1.0)
    else:
        x = max(x - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_X, x)

    if trilobot.read_button(trilobot.BUTTON_Y):
        y = min(y + 0.01, 1.0)
    else:
        y = max(y - 0.01, 0.0)
    trilobot.set_led(trilobot.LED_Y, y)

    time.sleep(0.01)
