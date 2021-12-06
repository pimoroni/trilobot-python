#!/usr/bin/env python3

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

loops = 10  # How many times to flash the LEDs

interval = 0.3  # Control the speed of the LED animation
tbot = Trilobot()

# Cycle R, G, B a set number of times
for i in range(loops):
    print(i)
    tbot.fill_underlighting(RED)
    time.sleep(interval)

    tbot.fill_underlighting(GREEN)
    time.sleep(interval)

    tbot.fill_underlighting(BLUE)
    time.sleep(interval)

# Turn off underlighting
tbot.clear_underlighting()
