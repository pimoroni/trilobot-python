import trilobot
import atexit


tb = trilobot.Trilobot()
speed = 0.9
def off():
    tb.fill_underlighting(0, 0, 0)
    tb.show_underlighting()
    tb.disable_motors()

atexit.register(off)

# Start moving forward
tb.set_left_speed(speed)
tb.set_right_speed(speed)

while True:
    distance = tb.read_distance()
    # turn if we are too closer than 30cm
    if distance < 30:
        tb.set_right_speed(-speed)
    else:
        tb.set_right_speed(speed)
    # no sleep needed, distance sensor provides sleep
