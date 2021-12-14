#!/usr/bin/env python3

import time
from trilobot import Trilobot

"""
An example of how to set a calibration on a servo connected to Trilobot,
and have it move to exact angles.
"""
print("Trilobot Example: Calibtrated Servo\n")


SWEEPS = 10  # How many times to sweep the servo
INTERVAL = 0.01  # The time in seconds between each step of the sequence

tbot = Trilobot()
tbot.initialise_servo(-90, 90, 550, 2450)  # Example pulses that map to min and max angles

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

print("Now Sweep")

# Sweep the servo a set number of times
for i in range(SWEEPS):
    print("Sweep:", i)

    for i in range(-90, 90):
        tbot.set_servo_angle(i)
        time.sleep(0.01)

    for i in range(-90, 90):
        tbot.set_servo_angle(0 - i)
        time.sleep(INTERVAL)

print("Done")
