#!/usr/bin/env python3

import time
from trilobot import *

"""
A smoother chaser animation example on Trilobot's underlights, using fading on each light.

Press CTRL + C to exit.
"""
print("Trilobot Example: Underlight Fade Chaser\n")


# How many times the LEDs will be updated per second
UPDATES = 60

HUE = 0.0  # Red
WIDTH = 1.5
SPEED = 3 / UPDATES

MAPPING = [LIGHT_REAR_LEFT,
           LIGHT_MIDDLE_LEFT,
           LIGHT_FRONT_LEFT,
           LIGHT_FRONT_RIGHT,
           LIGHT_MIDDLE_RIGHT,
           LIGHT_REAR_RIGHT]

tbot = Trilobot()


# Maps a value from one range to another
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# Shows a band with a given width at the position on the leds
def chaser_band(position, width, hue):
    half_width = width / 2
    centre_position = map(position, -1.0, 1.0, 1.0 - half_width, float(NUM_UNDERLIGHTS) - 1.0 + half_width)
    if width > 0.0:
        band_pixels_start = centre_position - (half_width)
        band_pixels_end = centre_position + (half_width)

        # Go through each led
        for i in range(NUM_UNDERLIGHTS):
            i2 = i + 1
            if i2 <= band_pixels_end:
                if i2 <= band_pixels_start:
                    # Outside of the band
                    tbot.set_underlight_hsv(MAPPING[i], hue, 0.0, 0.0, show=False)
                elif i <= band_pixels_start:
                    # Transition into the band
                    val = map(band_pixels_start, float(i), float(i2), 1.0, 0.0)
                    tbot.set_underlight_hsv(MAPPING[i], hue, 1.0, val, show=False)
                else:
                    # Inside the band
                    tbot.set_underlight_hsv(MAPPING[i], hue, 1.0, 1.0, show=False)

            elif i <= band_pixels_end:
                # Transition out of the band
                val = map(band_pixels_end, float(i), float(i2), 0.0, 1.0)
                tbot.set_underlight_hsv(MAPPING[i], hue, 1.0, val, show=False)
            else:
                # Outside of the band
                tbot.set_underlight_hsv(MAPPING[i], hue, 0.0, 0.0, show=False)
        tbot.show_underlighting()


# Turn the underlighting off if it was still on from some past code
tbot.clear_underlighting()

position = 0.0
clockwise = True
while True:
    # Draw the band
    chaser_band(position, WIDTH, HUE)

    if clockwise:
        position += SPEED
        if position >= 1.0:
            clockwise = False
    else:
        position -= SPEED
        if position <= -1.0:
            clockwise = True

    time.sleep(1.0 / UPDATES)
