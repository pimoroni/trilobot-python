#!/usr/bin/env python3

import time
from trilobot import Trilobot

"""
An example of how to perform simple movements of Trilobot.
"""
print("Trilobot Example: Movement\n")


tbot = Trilobot()

# Demo each of the move methods
tbot.forward()
time.sleep(1)

tbot.backward()
time.sleep(1)

tbot.curve_forward_right()
time.sleep(1)

tbot.curve_forward_left()
time.sleep(1)

tbot.turn_right()
time.sleep(1)

tbot.forward(0.5)  # Half speed
time.sleep(1)

tbot.turn_left(0.5)  # Half speed
time.sleep(1)

tbot.curve_backward_right(0.75)  # Three quarters speed
time.sleep(1)

tbot.forward()  # Full speed
time.sleep(0.5)

tbot.coast()  # Come to a halt gently
time.sleep(1)

tbot.forward()
time.sleep(0.5)

tbot.stop()  # Apply the brakes
time.sleep(1.0)

print("Done")
