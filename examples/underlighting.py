#!/usr/bin/env python

import time
from trilobot import Trilobot

print("Trilobot Underlighting Demo\n")


trilobot = Trilobot()

print("Separate red, green, blue ...")

# Turn the underlighting off if it was still on from some past code
trilobot.fill_underlighting(0, 0, 0)
trilobot.show_underlighting()
time.sleep(0.5)

# Set underlighting using separate red, green, and blue values
trilobot.set_underlighting(trilobot.FRONT_LEFT, 255, 0, 0)      # Red
trilobot.set_underlighting(trilobot.MIDDLE_LEFT, 255, 255, 0)   # Yellow
trilobot.set_underlighting(trilobot.REAR_LEFT, 0, 255, 0)       # Green
trilobot.set_underlighting(trilobot.REAR_RIGHT, 0, 255, 255)    # Cyan
trilobot.set_underlighting(trilobot.MIDDLE_RIGHT, 0, 0, 255)    # Blue
trilobot.set_underlighting(trilobot.FRONT_RIGHT, 255, 0, 255)   # Magenta
trilobot.show_underlighting()
time.sleep(3)


print("Hex color codes ...")

# Turn the underlighting off using a color code
trilobot.fill_underlighting('#000000')
trilobot.show_underlighting()
time.sleep(0.5)

# Set underlighting using a using a color code
trilobot.set_underlighting(trilobot.FRONT_LEFT, '#ff0000')      # Red
trilobot.set_underlighting(trilobot.MIDDLE_LEFT, 'ffff00')      # Yellow
trilobot.set_underlighting(trilobot.REAR_LEFT, '#00ff00')       # Green
trilobot.set_underlighting(trilobot.REAR_RIGHT, '#00ffff')      # Cyan
trilobot.set_underlighting(trilobot.MIDDLE_RIGHT, '#0000ff')    # Blue
trilobot.set_underlighting(trilobot.FRONT_RIGHT, '#ff00ff')     # Magenta
trilobot.show_underlighting()
time.sleep(3)


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
trilobot.fill_underlighting(BLACK)
trilobot.show_underlighting()
time.sleep(0.5)

# Set underlighting using a list/tuple
trilobot.set_underlighting(trilobot.FRONT_LEFT, RED)
trilobot.set_underlighting(trilobot.MIDDLE_LEFT, YELLOW)
trilobot.set_underlighting(trilobot.REAR_LEFT, GREEN)
trilobot.set_underlighting(trilobot.REAR_RIGHT, CYAN)
trilobot.set_underlighting(trilobot.MIDDLE_RIGHT, BLUE)
trilobot.set_underlighting(trilobot.FRONT_RIGHT, MAGENTA)
trilobot.show_underlighting()
time.sleep(3)

print("Done")
