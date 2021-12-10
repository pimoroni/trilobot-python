#!/usr/bin/env python3

from trilobot import Trilobot, BUTTON_A

"""
Shows how to read one of Trilobots buttons and tell if it was pressed or released.

Press CTRL + C to exit.
"""
print("Trilobot Example: Single Button\n")


tbot = Trilobot()

last_state = False
while True:
    # Read the button
    button_state = tbot.read_button(BUTTON_A)

    # Is the button state is different from when we last checked?
    if button_state != last_state:

        # Say if the button was pressed or released
        if button_state:
            print("Button A has been pressed")
        else:
            print("Button A has been released")

        # Turn the button's neighboring LED on or off
        tbot.set_button_led(BUTTON_A, button_state)

        # Update our record of the button state
        last_state = button_state
