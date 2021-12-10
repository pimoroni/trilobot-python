#!/usr/bin/env python3

import time
from trilobot import Trilobot, NUM_BUTTONS

"""
Shows how to control the brightness of the button LEDs, by having them fade up and down.
"""
print("Trilobot Example: Fade Button LEDs\n")


FADES = 10  # How many times to fade the LEDs
INTERVAL = 0.01  # The time in seconds between each step of the sequence
MAX_BRIGHTNESS = 1.0  # The maximum brightness to set the LEDs
STEPS = 100  # The number of steps to go between brightness levels. Must not be zero

tbot = Trilobot()

# Fade the button LEDs a set number of times
for i in range(FADES):
    print("Fade:", i)

    # Increase the brightness of the button LEDs from zero to max
    for step in range(STEPS):
        brightness = (MAX_BRIGHTNESS * step) / (STEPS - 1)

        # Set all the button LEDs to the new brightness
        for i in range(NUM_BUTTONS):
            tbot.set_button_led(i, brightness)

        time.sleep(INTERVAL)

    # Reduce the brightness of the button LEDs from max to zero
    for step in range(STEPS):
        brightness = 1.0 - ((MAX_BRIGHTNESS * step) / (STEPS - 1))

        # Set all the button LEDs to the new brightness
        for i in range(NUM_BUTTONS):
            tbot.set_button_led(i, brightness)

        time.sleep(INTERVAL)

print("Done")
