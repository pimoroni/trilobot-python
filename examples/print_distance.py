import time
from trilobot import Trilobot


if __name__ == '__main__':
    tb = Trilobot()
    while True:
        distance = tb.sense_distance_mm(timeout=600)
        print("Distance is {} mm".format(distance))
        time.sleep(0.01)
