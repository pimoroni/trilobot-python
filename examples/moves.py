#!/usr/bin/env python3

import time
from trilobot import Trilobot

print("Trilobot Movement Demo\n")

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

# Half speed
tbot.forward(0.5)
time.sleep(1)

tbot.turn_left(0.5)
time.sleep(1)

tbot.curve_backward_right(0.75)
time.sleep(1)

# Full speed
tbot.forward()
time.sleep(0.5)

# Come to a halt gently
tbot.coast()
time.sleep(1)

# Full speed
tbot.forward()
time.sleep(0.5)

# Apply the brakes
tbot.stop()
time.sleep(1.0)
