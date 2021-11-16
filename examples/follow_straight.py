import time
from trilobot import Trilobot

print("Trilobot Follow Straight Demo\n")

tb = Trilobot()
top_speed = 0.7         # The top speed (between 0.0 and 1.0) that the robot will drive at to get an object in range
goal_distance = 20.0    # The distance in cm the robot will keep an object in front of it
speed_range = 5.0       # The distance an object is from the goal that will have the robot drive at full speed

while True:
    distance = tb.read_distance()
                
    if distance >= 0.0:
        scale = (distance - goal_distance) / speed_range
        speed = max(min(scale, 1.0), -1.0) * top_speed
        print("Distance is {:.1f} cm. Speed is {:.2f}".format(distance, speed))
        tb.set_left_speed(speed)
        tb.set_right_speed(speed)
    else:
        tb.disable_motors()    
    
    time.sleep(0.01)
