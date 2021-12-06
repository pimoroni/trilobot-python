#!/usr/bin/env python3

import time
from trilobot import Trilobot, NUM_BUTTONS

"""
Flash the button LEDs.
"""

print("Trilobot Flash Button LEDs Example\n")

loops = 10  # How many times to flash the LEDs

interval = 0.3  # Control the speed of the LED animation

tbot = Trilobot()

# Flash the button LEDs a set number of times
for i in range(loops):
    print("Loop:", i)
    for led in range(NUM_BUTTONS):
        tbot.set_button_led(led, True)
    time.sleep(interval)

    for led in range(NUM_BUTTONS):
        tbot.set_button_led(led, False)
    time.sleep(interval)
