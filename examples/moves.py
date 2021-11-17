import time
from trilobot import Trilobot

print("Trilobot movement Demo\n")

tbot = Trilobot()

# Demo each of the move methods
tbot.forwards()
time.sleep(1)

tbot.reverse()
time.sleep(1)

tbot.curve_right()
time.sleep(1)

tbot.curve_left()
time.sleep(1)

tbot.turn_right()
time.sleep(1)

# Half speed
tbot.forwards(0.5)
time.sleep(1)

tbot.turn_left(0.5)
time.sleep(1)

tbot.curve_right(-0.75)
time.sleep(1)

# Full speed
tbot.forwards()
time.sleep(0.5)

# Come to a halt gently
tbot.coast()
time.sleep(1)

# Full speed
tbot.forwards()
time.sleep(0.5)

# Apply the brakes
tbot.stop()