#!/usr/bin/env python3

import time
from trilobot import Trilobot, BUTTON_A

"""
A demonstration of Trilobot's ultrasound sensor that has it keep an object
a goal distance in front of it. If the object gets closer Trilobot will reverse,
if the object gets further away Trilobot will drive forward.

Stop the example by pressing button A.
"""
print("Trilobot Example: Follow Straight\n")


TOP_SPEED = 0.7         # The top speed (between 0.0 and 1.0) that the robot will drive at to get an object in range
GOAL_DISTANCE = 20.0    # The distance in cm the robot will keep an object in front of it
SPEED_RANGE = 5.0       # The distance an object is from the goal that will have the robot drive at full speed

tbot = Trilobot()

while not tbot.read_button(BUTTON_A):
    distance = tbot.read_distance()

    if distance >= 0.0:
        scale = (distance - GOAL_DISTANCE) / SPEED_RANGE
        speed = max(min(scale, 1.0), -1.0) * TOP_SPEED
        print("Distance is {:.1f} cm. Speed is {:.2f}".format(distance, speed))

        tbot.set_motor_speeds(speed, speed)
    else:
        tbot.disable_motors()

    time.sleep(0.01)
