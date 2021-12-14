#!/usr/bin/env python3

from trilobot import Trilobot, BUTTON_A

"""
Further demonstrating Trilobot's ultrasound distance sensor, this example will drive
forward and then turn right to avoid obstacles it detects them with the sensor.

Stop the example by pressing button A.
"""
print("Trilobot Example: Avoid Walls\n")


SPEED = 0.7  # The speed to drive at
TURN_DISTANCE = 30  # How close a wall needs to be, in cm, before we start turning

tbot = Trilobot()

# Start moving forward
tbot.forward(SPEED)

while not tbot.read_button(BUTTON_A):
    distance = tbot.read_distance()

    # Turn if we are too closer than the turn distance
    if distance < TURN_DISTANCE:
        tbot.turn_right(SPEED)
    else:
        tbot.forward(SPEED)
    # No sleep is needed, as distance sensor provides sleep
