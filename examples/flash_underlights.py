#!/usr/bin/env python3

import time
from trilobot import Trilobot

"""
This example will demonstrate the RGB underlights of Trilobot,
by making them flash in a red, green and blue sequence.
"""
print("Trilobot Example: Flash Underlights\n")


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

LOOPS = 10  # How many times to play the LED animation
INTERVAL = 0.3  # Control the speed of the LED animation

tbot = Trilobot()

# Cycle R, G, B a set number of times
for i in range(LOOPS):
    print("Loop:", i)

    tbot.fill_underlighting(RED)
    time.sleep(INTERVAL)

    tbot.fill_underlighting(GREEN)
    time.sleep(INTERVAL)

    tbot.fill_underlighting(BLUE)
    time.sleep(INTERVAL)

# Turn off underlighting
tbot.clear_underlighting()

print("Done")
