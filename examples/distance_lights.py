#!/usr/bin/env python3

import time
from trilobot import Trilobot, BUTTON_A

"""
This brings together the underlights and the distance sensor, using the underlights
to indicate if something is too close with red, orange, green indications.
It also prints distances on the console.

Stop the example by pressing button A.
"""
print("Trilobot Example: Distance Lights\n")


BAND1 = 20  # Distance where lights show yellow
BAND2 = 80  # Distance where lights show yellow-green
BAND3 = 100  # Distance where lights show green

YELLOW_GREEN_POINT = 192  # The amount of red to show for the mid-point between green and yellow

tbot = Trilobot()


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

    if distance > BAND3:
        # Show green lights for distance over band3
        g = 255
    elif distance > BAND2:
        # Set colour fading from green-yellow to green between distance bands 2 and 3
        band_min = BAND2
        band_max = BAND3
        r = int(YELLOW_GREEN_POINT - YELLOW_GREEN_POINT * (distance - band_min) / (band_max - band_min))
        g = 255
    elif distance > BAND1:
        # Set colour fading from yellow to green-yellow between distance bands 1 and 2
        band_min = BAND1
        band_max = BAND2
        r = int(255 - (255 - YELLOW_GREEN_POINT) * (distance - band_min) / (band_max - band_min))
        g = 255
    elif distance > 0:
        # Set colour fading from red at 0cm to yellow at distance band1
        band_max = BAND1 * BAND1
        r = 255
        g = int(255 * distance * BAND1 / band_max)
    else:
        # Red for closest distance
        r = 255

    return (r, g, b)


while not tbot.read_button(BUTTON_A):

    distance = tbot.read_distance()
    print("Distance is {:.1f} cm".format(distance))

    rgb_colour = colour_from_distance(distance)
    tbot.fill_underlighting(rgb_colour)

    time.sleep(0.1)
