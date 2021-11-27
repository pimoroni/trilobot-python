#!/usr/bin/env python

import time
from trilobot import Trilobot

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
while True:
    for i in range(-90, 90):
        tbot.set_servo_angle(i)
        time.sleep(0.01)

    for i in range(-90, 90):
        tbot.set_servo_angle(0 - i)
        time.sleep(0.01)
