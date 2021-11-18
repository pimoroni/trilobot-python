import time
from trilobot import Trilobot, BUTTON_A

print("Trilobot Print Distance Demo\n")

tbot = Trilobot()

while not tbot.read_button(BUTTON_A):

    # Take 10 measurements rapidly
    for i in range(10):
        clock_check = time.perf_counter()
        distance = tbot.read_distance(timeout=25, samples=3)
        print("Rapid:  Distance is {:.1f} cm (took {:.4f} sec)".format(distance, (time.perf_counter() - clock_check)))
        time.sleep(0.01)

    # Take 10 measurements allowing longer time for measuring greater distances
    for i in range(10):
        clock_check = time.perf_counter()
        distance = tbot.read_distance(timeout=200, samples=9)
        print("Slower: Distance is {:.1f} cm (took {:.4f} sec)".format(distance, (time.perf_counter() - clock_check)))
        time.sleep(0.01)
