import time
from trilobot import Trilobot


tb = Trilobot()
top_speed = 0.7
goal_distance = 20.0    # The distance in cm the robot will keep an object in front of it
goal_threshold = 5.0    # How far from the goal an object should be before the robot will chase after it
speed_range = 5.0       # The distance an object is from the goal that will have the robot drive at full speed
switching_time = 0.3

arc_left = True

last_time = time.perf_counter()
while True:
    distance = tb.read_distance()
    
            
    if distance >= 0.0:
        spd = 0.0
        if distance > goal_distance + goal_threshold:
            spd = min((distance - (goal_distance + goal_threshold)) / speed_range, 1.0) * top_speed
        elif  distance < goal_distance - goal_threshold:
            spd = max((distance - (goal_distance - goal_threshold)) / speed_range, -1.0) * top_speed
        print("Distance is {:.1f} cm. Speed is {:.2f}".format(distance, spd))
        if arc_left:
            tb.set_left_speed(0.0)
            tb.set_right_speed(spd)    
        else:   # Arc Right
            tb.set_left_speed(spd)
            tb.set_right_speed(0.0)

    current_time = time.perf_counter()
    if current_time > last_time + switching_time:
        arc_left = not arc_left
        last_time = current_time
    
    time.sleep(0.01)
