#!/usr/bin/env python3

import time
from trilobot import *

"""
Examples of how to set Trilobot's underlights to different colors and
have them all show at the same time.
"""
print("Trilobot Example: Show Underlighting\n")


SHOW_TIME = 3  # How long in seconds to have each pattern visible for
CLEAR_TIME = 0.5  # How long in seconds to have the underlights off between each pattern

tbot = Trilobot()

print("Separate red, green, blue ...")

# Turn the underlighting off using separate red, green, and blue values
tbot.fill_underlighting(0, 0, 0)  # Black
time.sleep(CLEAR_TIME)

# Set underlighting using separate red, green, and blue values
tbot.set_underlight(LIGHT_FRONT_LEFT, 255, 0, 0, show=False)      # Red
tbot.set_underlight(LIGHT_MIDDLE_LEFT, 255, 255, 0, show=False)   # Yellow
tbot.set_underlight(LIGHT_REAR_LEFT, 0, 255, 0, show=False)       # Green
tbot.set_underlight(LIGHT_REAR_RIGHT, 0, 255, 255, show=False)    # Cyan
tbot.set_underlight(LIGHT_MIDDLE_RIGHT, 0, 0, 255, show=False)    # Blue
tbot.set_underlight(LIGHT_FRONT_RIGHT, 255, 0, 255, show=False)   # Magenta
tbot.show_underlighting()
time.sleep(SHOW_TIME)


print("Hex color codes ...")

# Turn the underlighting off using a color code
tbot.fill_underlighting('#000000')  # Black
time.sleep(CLEAR_TIME)

# Set underlighting using a using a color code
tbot.set_underlight(LIGHT_FRONT_LEFT, '#ff0000', show=False)      # Red
tbot.set_underlight(LIGHT_MIDDLE_LEFT, 'ffff00', show=False)      # Yellow
tbot.set_underlight(LIGHT_REAR_LEFT, '#00ff00', show=False)       # Green
tbot.set_underlight(LIGHT_REAR_RIGHT, '#00ffff', show=False)      # Cyan
tbot.set_underlight(LIGHT_MIDDLE_RIGHT, '#0000ff', show=False)    # Blue
tbot.set_underlight(LIGHT_FRONT_RIGHT, '#ff00ff', show=False)     # Magenta
tbot.show_underlighting()
time.sleep(SHOW_TIME)


print("Lists/Tuples ...")

# Define some common colours to use later
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)

# Turn the underlighting off using a list/tuple
tbot.fill_underlighting(BLACK)
time.sleep(CLEAR_TIME)

# Set underlighting using a list/tuple
tbot.set_underlight(LIGHT_FRONT_LEFT, RED, show=False)
tbot.set_underlight(LIGHT_MIDDLE_LEFT, YELLOW, show=False)
tbot.set_underlight(LIGHT_REAR_LEFT, GREEN, show=False)
tbot.set_underlight(LIGHT_REAR_RIGHT, CYAN, show=False)
tbot.set_underlight(LIGHT_MIDDLE_RIGHT, BLUE, show=False)
tbot.set_underlight(LIGHT_FRONT_RIGHT, MAGENTA, show=False)
tbot.show_underlighting()
time.sleep(SHOW_TIME)

print("Hue / Sat / Val ...")

# Turn the underlighting off using a list/tuple
tbot.fill_underlighting_hsv(0.0, 0.0, 0.0)  # Black
time.sleep(CLEAR_TIME)

# Set underlighting using a list/tuple
tbot.set_underlight_hsv(LIGHT_FRONT_LEFT, 0 / 6, 1.0, 1.0, show=False)    # Red
tbot.set_underlight_hsv(LIGHT_MIDDLE_LEFT, 1 / 6, 1.0, 1.0, show=False)   # Yellow
tbot.set_underlight_hsv(LIGHT_REAR_LEFT, 2 / 6, 1.0, 1.0, show=False)     # Green
tbot.set_underlight_hsv(LIGHT_REAR_RIGHT, 3 / 6, 1.0, 1.0, show=False)    # Cyan
tbot.set_underlight_hsv(LIGHT_MIDDLE_RIGHT, 4 / 6, 1.0, 1.0, show=False)  # Blue
tbot.set_underlight_hsv(LIGHT_FRONT_RIGHT, 5 / 6, 1.0, 1.0, show=False)   # Magenta
tbot.show_underlighting()
time.sleep(SHOW_TIME)

# Turn the underlighting off using clear
tbot.clear_underlighting()

print("Done")
