import time
from trilobot import Trilobot

band1 = 20 # Distance where lights show yellow
band2 = 80 # Distance where lights show yellow-green
band3 = 100 # Distance where lights show green

yellowgreenpoint = 192
orangepoint = 178

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
            bandmin = band2
            bandmax = band3
            r = int(yellowgreenpoint - yellowgreenpoint * (distance - bandmin) / (bandmax - bandmin))
            g = 255
        elif distance > band1:
            # Set colour fading from yellow to green-yellow between distance band1-band2
            bandmin = band1
            bandmax = band2
            r = int(255 - (255 - yellowgreenpoint) * (distance - bandmin) / (bandmax - bandmin))
            g = 255
        elif distance > 0:
            # Set colour fading from red at 0cm to yellow at distance band1
            bandmax = band1 * band1
            r = 255
            g = int(255 * distance * band1 / bandmax)
        else:
            # Red for closest distance
            r = 255

        print(r,g,b,distance)
        return (r,g,b)

if __name__ == '__main__':
    tb = Trilobot()
    
    while not tb.read_button(tb.BUTTON_A):

        distance = tb.read_distance()

        rgb_colour = colour_from_distance(distance)
        tb.fill_underlighting(rgb_colour)
        tb.show_underlighting()

        time.sleep(0.1)
