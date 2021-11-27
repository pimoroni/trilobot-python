
from trilobot import Trilobot

tbot = Trilobot()
BUTTON_A = 0

print("Demo of Trilobot's buttons")

buttonStatus = [False, False, False, False]
lastButtonStatus = [False, False, False, False]
buttonNames = ["A", "B", "X", "Y"]

while True:

    for i in range(0,4):
        buttonStatus[i] = tbot.read_button(i)
        if buttonStatus[i] != lastButtonStatus[i]:
            if buttonStatus[i]:
                print(f"Button {buttonNames[i]} is pressed")
                lastButtonStatus[i] = True
                tbot.set_led(i, 0.5)
            else:
                print(f"Button {buttonNames[i]} has been released")
                lastButtonStatus[i] = False
                tbot.set_led(i, 0.0)
