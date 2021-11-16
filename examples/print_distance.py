import time
from trilobot import Trilobot


if __name__ == '__main__':
    tb = Trilobot()
    
    while True:

        #Take 10 measurements rapidly for shorter distances
        for i in range(100):
            clockcheck = time.perf_counter()
            distance = tb.read_distance(timeout=25, samples=3)
            print("Rapid:  Distance is {:.1f} cm (took {:.4f} sec)".format(distance,(time.perf_counter() - clockcheck) ) )
            time.sleep(0.01)

        #Take 10 measurements slower for longer distances
        for i in range(100):
            clockcheck = time.perf_counter()
            distance = tb.read_distance(timeout=200, samples=5)
            print("Slower: Distance is {:.1f} cm (took {:.4f} sec)".format(distance,(time.perf_counter() - clockcheck) ) )
            time.sleep(0.01)


