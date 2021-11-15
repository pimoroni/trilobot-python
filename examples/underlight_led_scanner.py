"""Make an LED scanning animation with the underlighting"""
import trilobot
import time
import atexit

interval = 0.1 # control the speed of the LED animation
tb = trilobot.Trilobot()

def off():
    """A quick shortcut to turn everything off"""
    tb.fill_underlighting(0, 0, 0)
    tb.show_underlighting()

atexit.register(off)

# Map so 0-5 goes from left to right.
mapping = [tb.REAR_RIGHT, tb.REAR_LEFT, tb.MIDDLE_LEFT, tb.FRONT_LEFT, tb.FRONT_RIGHT, tb.MIDDLE_RIGHT]

while True:
    for n in range(0, 5):
        phy_led = mapping[n]
        tb.fill_underlighting(0, 0, 0)
        tb.set_underlighting(phy_led, 1, 0, 0)
        tb.show_underlighting()
        time.sleep(interval)

    for n in range(5, 0, -1):
        phy_led = mapping[n]
        tb.fill_underlighting(0, 0, 0)
        tb.set_underlighting(phy_led, 1, 0, 0)
        tb.show_underlighting()
        time.sleep(interval)
