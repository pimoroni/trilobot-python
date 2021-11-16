import time
from trilobot import Trilobot


if __name__ == '__main__':
    tb = Trilobot()
    
    while not tb.read_button(tb.BUTTON_A):

        distance = tb.read_distance()

        # Set light colour based on distance
        if distance > 100:
            # Show lights green for over 100cm
            tb.fill_underlighting(0, 1.0, 0)
        elif distance > 30:
            # Set colour fading from yellow at 30cm to green at 100cm
            tb.fill_underlighting(1.0 - (distance - 30) / 70, 1.0, 0)
        elif distance > 0:
            # Set colour fading from red at 0cm to yellow at 30cm
            tb.fill_underlighting(1.0, distance / 30, 0)
        else:
            # Red for closest distance
            tb.fill_underlighting(1.0, 0, 0)

        tb.show_underlighting()

        time.sleep(0.1)
