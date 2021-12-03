#!/usr/bin/env python

import time
from trilobot import Trilobot, NUM_LEDS

"""
Flash the underlighting LEDs red, green and blue.
Will turn them off when exited.
"""

print("Trilobot Test LEDs Demo\n")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

interval = 0.3  # control the speed of the LED animation
tbot = Trilobot()

# Cycle R, G, B 10 times.
for i in range(0, 10):
    print(i)
    tbot.fill_underlighting(RED)
    time.sleep(interval)

    tbot.fill_underlighting(GREEN)
    time.sleep(interval)

    tbot.fill_underlighting(BLUE)
    time.sleep(interval)

# turn off underlighting

tbot.fill_underlighting(BLACK)

# flash the button LEDs at 50% 10 times

for i in range(0, 10):
    print(i)
    for led in range(NUM_LEDS):
        tbot.set_led(led, 0.5)
    time.sleep(interval)
    for led in range(NUM_LEDS):
        tbot.set_led(led, 0)
    time.sleep(interval)
