#!/usr/bin/env python3

import time
from trilobot import Trilobot, NUM_BUTTONS

"""
Has the button LEDs fade up and down over time.
"""

print("Trilobot Fade Button LEDs Example\n")

tbot = Trilobot()

loops = 10  # How many times to fade the LEDs
max_brightness = 1.0  # The maximum brightness to set the LEDs
interval = 0.1  # The time in seconds between each step of the sequence
steps = 10  # The number of steps to go between brightness levels. Must not be zero

# Fade the button LEDs a set number of times
for i in range(loops):
	# Increase the brightness of the button LEDs from zero to max
	for step in range(steps):
		brightness = (max_brightness * step) / steps
		
		# Set all the button LEDs to the 
		for i in range(NUM_BUTTONS):
			tbot.set_button_led(i, brightness)
			
		time.sleep(interval)
			
	# Reduce the brightness of the button LEDs from max to zero
	for step in range(steps):
		brightness = 1.0 - ((max_brightness * step) / steps)
		
		# Loop through all of the button LEDs
		for i in range(NUM_BUTTONS):
			tbot.set_button_led(i, brightness)
			
		time.sleep(interval)
