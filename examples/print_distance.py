#!/usr/bin/env python3

import time

from trilobot import BUTTON_A, Trilobot

"""
This demonstrates how to read distance values from Trilobot's ultrasound
distance sensor. It will print the values it reads onto the console in cm,
along with the time taken to get the readings.

Stop the example by pressing button A.
"""
print("Trilobot Example: Print Distance\n")


tbot = Trilobot()

while not tbot.read_button(BUTTON_A):

    # Take 10 measurements rapidly
    for _i in range(10):
        clock_check = time.perf_counter()
        distance = tbot.read_distance(timeout=25, samples=3)
        print(f"Rapid:  Distance is {distance:.1f} cm (took {time.perf_counter() - clock_check:.4f} sec)")
        time.sleep(0.01)

    # Take 10 measurements allowing longer time for measuring greater distances
    for _i in range(10):
        clock_check = time.perf_counter()
        distance = tbot.read_distance(timeout=200, samples=9)
        print(f"Slower: Distance is {distance:.1f} cm (took {time.perf_counter() - clock_check:.4f} sec)")
        time.sleep(0.01)
