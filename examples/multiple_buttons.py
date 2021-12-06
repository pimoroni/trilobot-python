#!/usr/bin/env python3

from trilobot import Trilobot, NUM_BUTTONS

print("Trilobot Multiple Button Example")

tbot = Trilobot()

# The names to display for each button
button_names = ["A", "B", "X", "Y"]

last_state = [False, False, False, False]
while True:
	# Loop through all of the buttons
    for i in range(NUM_BUTTONS):
		# Read the current button
        button_state = tbot.read_button(i)
		
		# Is the button state is different from when we last checked?
        if button_state != last_state[i]:
		
			# Say if the button was pressed or released
            if button_state:
                print(f"Button {button_names[i]} has been pressed")
            else:
                print(f"Button {button_names[i]} has been released")
				
			# Turn the button's neighboring LED on or off
			tbot.set_button_led(i, button_state)
			
			# Update our record of the button state
			last_state[i] = button_state
