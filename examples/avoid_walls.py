#!/usr/bin/env python

from trilobot import Trilobot, BUTTON_A

print("Trilobot Avoid Walls Demo\n")

tbot = Trilobot()
speed = 0.9

# Start moving forward
tbot.forward(speed)

while not tbot.read_button(BUTTON_A):
    distance = tbot.read_distance()
    # turn if we are too closer than 30cm
    if distance < 30:
        tbot.set_right_speed(-speed)
    else:
        tbot.set_right_speed(speed)
    # no sleep needed, distance sensor provides sleep
