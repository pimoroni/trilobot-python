"""
Flash the underlighting LEDs red, green and blue.
Will turn them off when exited.
"""
import trilobot
import time
import atexit

interval = 0.3 # control the speed of the LED animation
tb = trilobot.Trilobot()

def off():
    """A quick shortcut to turn everything off"""
    tb.fill_underlighting(0, 0, 0)
    tb.show_underlighting()

# When the code exits - error, or completes, make sure the leds are off
atexit.register(off)

# Cycle R, G, B 10 times.
for i in range(0, 10):
    print(i)
    tb.fill_underlighting(255, 0, 0)
    tb.show_underlighting()
    time.sleep(interval)

    tb.fill_underlighting(0, 255, 0)
    tb.show_underlighting()
    time.sleep(interval)

    tb.fill_underlighting(0, 0, 255)
    tb.show_underlighting()
    time.sleep(interval)
