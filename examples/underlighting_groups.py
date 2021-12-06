#!/usr/bin/env python3

import time
from trilobot import *

"""
Examples of how to set Trilobot groups of underlights
"""

print("Trilobot Underlighting Groups Example\n")

show_time = 3  # How long in seconds to have each pattern visible for
clear_time = 0.5  # How long in seconds to have the underlights off between each pattern

# Define some common colours to use later
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

tbot = Trilobot()

print("Left and Right ...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(clear_time)

# Set underlighting using a group list/tuple
tbot.set_underlight(LIGHTS_LEFT, RED)
tbot.set_underlight(LIGHTS_RIGHT, GREEN)
time.sleep(show_time)

print("Front, Middle, and Rear ...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(clear_time)

# Set underlighting using a group list/tuple
tbot.set_underlight(LIGHTS_FRONT, RED)
tbot.set_underlight(LIGHTS_MIDDLE, GREEN)
tbot.set_underlight(LIGHTS_REAR, BLUE)
time.sleep(show_time)

print("Diagonals and Middle ...")

# Turn the underlighting off using a list/tuple
tbot.clear_underlighting()
time.sleep(clear_time)

# Set underlighting using a group list/tuple
tbot.set_underlight(LIGHTS_LEFT_DIAGONAL, RED)
tbot.set_underlight(LIGHTS_MIDDLE, GREEN)
tbot.set_underlight(LIGHTS_RIGHT_DIAGONAL, BLUE)
time.sleep(show_time)

# Turn the underlighting off
tbot.clear_underlighting()

print("Done")
