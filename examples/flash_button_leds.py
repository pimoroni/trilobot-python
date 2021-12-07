#!/usr/bin/env python3

import time
from trilobot import Trilobot, NUM_BUTTONS

"""
Shows how to turn the button LEDs on and off, by having them flash.
"""
print("Trilobot Example: Flash Button LEDs\n")


FLASHES = 10  # How many times to flash the LEDs
INTERVAL = 0.3  # Control the speed of the LED animation

tbot = Trilobot()

# Flash the button LEDs a set number of times
for i in range(FLASHES):
    print("Flash:", i)

    for led in range(NUM_BUTTONS):
        tbot.set_button_led(led, True)
    time.sleep(INTERVAL)

    for led in range(NUM_BUTTONS):
        tbot.set_button_led(led, False)
    time.sleep(INTERVAL)

print("Done")
