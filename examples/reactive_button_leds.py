#!/usr/bin/env python3

import time
from trilobot import *

"""
Shows how to use the buttons to make their neighbouring LEDs fade up
when pressed fade down when released.

Press CTRL + C to exit.
"""
print("Trilobot Example: Reactive Button LEDs\n")


tbot = Trilobot()

a = 0
b = 0
x = 0
y = 0
while True:

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
