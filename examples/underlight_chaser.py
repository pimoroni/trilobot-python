#!/usr/bin/env python3

import time
from trilobot import *

"""Make an LED scanning animation with the underlighting"""

print("Trilobot Underlight Chaser Demo\n")

interval = 0.1  # control the speed of the LED animation
tbot = Trilobot()

RED = (255, 0, 0)

# Map so 0-5 goes from left to right.
mapping = [LIGHT_REAR_LEFT,
		   LIGHT_MIDDLE_LEFT,
		   LIGHT_FRONT_LEFT,
		   LIGHT_FRONT_RIGHT,
		   LIGHT_MIDDLE_RIGHT,
		   LIGHT_REAR_RIGHT]

while True:
    for n in range(0, NUM_UNDERLIGHTS):
        phy_led = mapping[n]
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(phy_led, RED)
        time.sleep(interval)

    for n in range(NUM_UNDERLIGHTS, 0, -1):
        phy_led = mapping[n]
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(phy_led, RED)
        time.sleep(interval)
