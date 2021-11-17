#!/usr/bin/env python

import time
from trilobot import Trilobot

print("Trilobot LED Fading Chaser Demo\n")


trilobot = Trilobot()

# How many times the LEDs will be updated per second
UPDATES = 60

HUE = 0.0 # Red
WIDTH = 1.5
SPEED = 3 / UPDATES

led_mapping = [trilobot.REAR_LEFT,
               trilobot.MIDDLE_LEFT,
               trilobot.FRONT_LEFT,
               trilobot.FRONT_RIGHT,
               trilobot.MIDDLE_RIGHT,
               trilobot.REAR_RIGHT]

# Maps a value from one range to another
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# Shows a band with a given width at the position on the leds
def chaser_band(position, width, hue):
    half_width = width/2
    centre_position = map(position, -1.0, 1.0, 1.0 - half_width, float(trilobot.NUM_UNDERLIGHTS) - 1.0 + half_width)
    if width > 0.0:
        band_pixels_start = centre_position - (half_width)
        band_pixels_end = centre_position + (half_width)

        # Go through each led
        for i in range(trilobot.NUM_UNDERLIGHTS):
            i2 = i + 1
            if i2 <= band_pixels_end:
                if i2 <= band_pixels_start:
                    # Outside of the band
                    trilobot.set_underlighting_hsv(led_mapping[i], hue, 0.0, 0.0)
                elif i <= band_pixels_start:
                    # Transition into the band
                    val = map(band_pixels_start, float(i), float(i2), 1.0, 0.0)
                    trilobot.set_underlighting_hsv(led_mapping[i], hue, 1.0, val)
                else:
                    # Inside the band
                    trilobot.set_underlighting_hsv(led_mapping[i], hue, 1.0, 1.0)

            elif i <= band_pixels_end:
                # Transition out of the band
                val = map(band_pixels_end, float(i), float(i2), 0.0, 1.0)
                trilobot.set_underlighting_hsv(led_mapping[i], hue, 1.0, val)
            else:
                # Outside of the band
                trilobot.set_underlighting_hsv(led_mapping[i], hue, 0.0, 0.0)
                pass


# Turn the underlighting off if it was still on from some past code
trilobot.fill_underlighting(0, 0, 0)    # Black

position = 0.0
clockwise = True
while True:
    # Draw the band
    chaser_band(position, WIDTH, HUE)
    trilobot.show_underlighting()

    if clockwise:
        position += SPEED
        if position >= 1.0:
            clockwise = False
    else:
        position -= SPEED
        if position <= -1.0:
            clockwise = True

    time.sleep(1.0 / UPDATES)