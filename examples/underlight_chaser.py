#!/usr/bin/env python3

import time
from trilobot import *

"""
An example chaser animation using Trilobot's underlighting.

Press CTRL + C to exit.
"""

print("Trilobot Example: Underlight Chaser\n")


INTERVAL = 0.1  # control the speed of the LED animation

RED = (255, 0, 0)

# Map so 0-5 goes from left to right.
MAPPING = [LIGHT_REAR_LEFT,
           LIGHT_MIDDLE_LEFT,
           LIGHT_FRONT_LEFT,
           LIGHT_FRONT_RIGHT,
           LIGHT_MIDDLE_RIGHT,
           LIGHT_REAR_RIGHT]

tbot = Trilobot()

while True:
    for n in range(0, NUM_UNDERLIGHTS - 1):
        phy_led = MAPPING[n]
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(phy_led, RED)
        time.sleep(INTERVAL)

    for n in range(NUM_UNDERLIGHTS - 1, 0, -1):
        phy_led = MAPPING[n]
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(phy_led, RED)
        time.sleep(INTERVAL)
