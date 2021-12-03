#!/usr/bin/env python3

from trilobot import Trilobot, BUTTON_A

tbot = Trilobot()

print("Demo of Trilobot's buttons")


last_button_status = False
while True:
    button_status = tbot.read_button(BUTTON_A)
    if button_status != last_button_status:
        if button_status:
            print("Button A is pressed")
            last_button_status = True
            tbot.set_led(BUTTON_A, 0.5)
        else:
            print("Button A has been released")
            last_button_status = False
            tbot.set_led(BUTTON_A, 0.0)
