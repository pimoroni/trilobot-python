
from trilobot import Trilobot

tbot = Trilobot()
BUTTON_A = 0

print("Demo of Trilobot's buttons")


lastButtonStatus = False
while True:

    buttonStatus = tbot.read_button(BUTTON_A)
    if buttonStatus != lastButtonStatus:
        if buttonStatus:
            print("Button A is pressed")
            lastButtonStatus = True
            tbot.set_led(BUTTON_A, 0.5)
        else:
            print("Button A has been released")
            lastButtonStatus = False
            tbot.set_led(BUTTON_A, 0.0)
