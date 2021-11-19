#!/usr/bin/env python

import time
from trilobot import Trilobot

"""
Flash the underlighting LEDs red, green and blue.
Will turn them off when exited.
"""

print("Trilobot Test LEDs Demo\n")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

interval = 0.3  # control the speed of the LED animation
tbot = Trilobot()

# Cycle R, G, B 10 times.
for i in range(0, 10):
    print(i)
    tbot.fill_underlighting(RED)
    time.sleep(interval)

    tbot.fill_underlighting(GREEN)
    time.sleep(interval)

    tbot.fill_underlighting(BLUE)
    time.sleep(interval)
