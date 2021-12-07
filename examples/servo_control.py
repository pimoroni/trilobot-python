#!/usr/bin/env python3

import math
import time
from trilobot import Trilobot

"""
An example of how to command a servo connected to Trilobot to move and perform sweeping motions.
"""
print("Trilobot Example: Servo Control\n")

SWEEPS = 5  # How many sweeps of the servo to perform
STEPS = 10  # The number of discrete sweep steps
STEPS_INTERVAL = 0.5  # The time in seconds between each step of the sequence

tbot = Trilobot()

print("Go to center")
tbot.servo_to_center()
time.sleep(2)

print("Go to min")
tbot.servo_to_min()
time.sleep(2)

print("Go to max")
tbot.servo_to_max()
time.sleep(2)

print("And back to center")
tbot.servo_to_center()
time.sleep(2)

print("Servo Off")
tbot.disable_servo()

print("Now Sweep", SWEEPS, "Times")
for j in range(SWEEPS):
    print("Sine Sweep:", j)

    for i in range(360):
        tbot.set_servo_value(math.sin(math.radians(i)))
        time.sleep(0.01)

print("Now Sweep", SWEEPS, "Times, in descrete steps")
for j in range(SWEEPS):
    print("Discrete Sweep:", j)

    for i in range(0, STEPS):
        tbot.servo_to_percent(i, 0, STEPS, 0)
        time.sleep(STEPS_INTERVAL)
    for i in range(0, STEPS):
        tbot.servo_to_percent(i, STEPS, 0, 0)
        time.sleep(STEPS_INTERVAL)

print("Done")
