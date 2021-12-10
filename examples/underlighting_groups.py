#!/usr/bin/env python3

import time
from trilobot import *

"""
Examples of how to set multiple Trilobot underlights to a color with one command.
"""
print("Trilobot Example: Underlighting Groups\n")


SHOW_TIME = 3  # How long in seconds to have each pattern visible for
CLEAR_TIME = 0.5  # How long in seconds to have the underlights off between each pattern

# Define some common colours to use later
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tbot = Trilobot()

print("Left and Right ...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(CLEAR_TIME)

# Set underlighting using a group list/tuple
tbot.set_underlights(LIGHTS_LEFT, RED)
tbot.set_underlights(LIGHTS_RIGHT, GREEN)
time.sleep(SHOW_TIME)

print("Front, Middle, and Rear ...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(CLEAR_TIME)

# Set underlighting using a group list/tuple
tbot.set_underlights(LIGHTS_FRONT, RED)
tbot.set_underlights(LIGHTS_MIDDLE, GREEN)
tbot.set_underlights(LIGHTS_REAR, BLUE)
time.sleep(SHOW_TIME)

print("Diagonals and Middle ...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(CLEAR_TIME)

# Set underlighting using a group list/tuple
tbot.set_underlights(LIGHTS_LEFT_DIAGONAL, RED)
tbot.set_underlights(LIGHTS_MIDDLE, GREEN)
tbot.set_underlights(LIGHTS_RIGHT_DIAGONAL, BLUE)
time.sleep(SHOW_TIME)

print("Front, Middle, and Rear HSV...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(CLEAR_TIME)

# Set underlighting using a group list/tuple
tbot.set_underlights_hsv(LIGHTS_FRONT, 0)
tbot.set_underlights_hsv(LIGHTS_MIDDLE, 1 / 3)
tbot.set_underlights_hsv(LIGHTS_REAR, 2 / 3)
time.sleep(SHOW_TIME)

# Turn the underlighting off
tbot.clear_underlights(LIGHTS_FRONT)
time.sleep(CLEAR_TIME)
tbot.clear_underlights(LIGHTS_MIDDLE)
time.sleep(CLEAR_TIME)
tbot.clear_underlights(LIGHTS_REAR)
time.sleep(CLEAR_TIME)

print("Done")
