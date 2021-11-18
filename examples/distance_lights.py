#!/usr/bin/env python

import time
from trilobot import Trilobot, BUTTON_A

print("Trilobot Distance Lights Demo\n")

band1 = 20  # Distance where lights show yellow
band2 = 80  # Distance where lights show yellow-green
band3 = 100  # Distance where lights show green

yellow_green_point = 192
orange_point = 178


def colour_from_distance(distance):
    """ Returns a colour based on distance, fading from green at > 100cm
        through to red at 0cm. Sets the yellow point at 20cm rather than
        half way as this gives a better indication of close objects. The
        fade from red to yellow uses the square of the distance so the red
        does not dominate the yellow over most of the < 20cm range.
    """
    r = 0
    g = 0
    b = 0

    if distance > band3:
        # Show lights green for over distance band3
        g = 255
    elif distance > band2:
        # Set colour fading from green-yellow to green between distance band2-band3
        band_min = band2
        band_max = band3
        r = int(yellow_green_point - yellow_green_point * (distance - band_min) / (band_max - band_min))
        g = 255
    elif distance > band1:
        # Set colour fading from yellow to green-yellow between distance band1-band2
        band_min = band1
        band_max = band2
        r = int(255 - (255 - yellow_green_point) * (distance - band_min) / (band_max - band_min))
        g = 255
    elif distance > 0:
        # Set colour fading from red at 0cm to yellow at distance band1
        band_max = band1 * band1
        r = 255
        g = int(255 * distance * band1 / band_max)
    else:
        # Red for closest distance
        r = 255

    return (r, g, b)


tbot = Trilobot()

while not tbot.read_button(BUTTON_A):

    distance = tbot.read_distance()
    print("Distance is {:.1f} cm".format(distance))

    rgb_colour = colour_from_distance(distance)
    tbot.fill_underlighting(rgb_colour)

    time.sleep(0.1)
