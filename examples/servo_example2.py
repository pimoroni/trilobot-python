import time
import math
from trilobot import *

tbot = Trilobot()

# tbot.enable_servo(SERVO_MIN, SERVO_MAX)
tbot.enable_servo()   # defaults to 2.5 which equates to 0 degrees and 12.5 roughly 180 degrees

try:
	# delay set to None will not stop the servo after each move, 
	# setting to a small value (like 0.25) will move then stop the servo to avoid jitter
	delay = None
	print("Servo moving through min, mid and max points")
	print("With no delay (None) then with quarter of a second (0.25) to reduce jitter")
	for test in range(0,2):		
		tbot.set_servo(SERVO_MIN, delay)
		time.sleep(2)
		tbot.set_servo(SERVO_MID, delay)
		time.sleep(2)
		tbot.set_servo(SERVO_MAX, delay)
		time.sleep(2)
		# Now set the delay t the default and notice the jitter is much reduced.		
		delay = SERVO_DELAY
	
	# setting the servo to a specific angle between 0 and 180
	# (use the enable_servo method to increase this beyond the default)
	print("Set to a specific angle")
	for test in range(0,2):		
		for angle in range(0,180,10):
			tbot.set_servo_angle(angle)
			time.sleep(0.5)
			
	# smooth sine curve
	tbot.set_servo()	
	
	print("Sine motion using interpolation")
	for test in range(0,2):		
		for i in range(0, 360):
			angle = math.sin(math.radians(i))
			# Map the -1 to +1 range to the minimum and maxim servo range
			res = tbot.interpolate(angle,-1,1,SERVO_MIN,SERVO_MAX)   
			# Now move the servo to that position and wait for 0.01 seconds before stopping the servo. 
			tbot.set_servo(res, 0.01)            
	
		
	
except KeyboardInterrupt:
  tbot.disable_servo()
