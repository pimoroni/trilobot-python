#!/usr/bin/env python3

from trilobot import Trilobot, NUM_BUTTONS

tbot = Trilobot()

print("Demo of Trilobot's buttons")

button_status = [False, False, False, False]
last_button_status = [False, False, False, False]
button_names = ["A", "B", "X", "Y"]

while True:
    for i in range(NUM_BUTTONS):
        button_status[i] = tbot.read_button(i)
        if button_status[i] != last_button_status[i]:
            if button_status[i]:
                print(f"Button {button_names[i]} is pressed")
                last_button_status[i] = True
                tbot.set_led(i, 0.5)
            else:
                print(f"Button {button_names[i]} has been released")
                last_button_status[i] = False
                tbot.set_led(i, 0.0)
