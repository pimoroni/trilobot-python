from gpiozero import Servo
import math
import os
import sys
from time import sleep

# if not exists /var/run/pigpio.pid:
#    stop now
if not os.path.isfile('/var/run/pigpio.pid'):
    print('Please install pigpio with "sudo apt install pigpio"')
    print('Then run "sudo pigpiod" to enable')
    sys.exit()

from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()
servo = Servo(12, min_pulse_width=0.5 / 1000, max_pulse_width=2.5 / 1000, pin_factory=factory)

print("Go to middle")
servo.mid()
sleep(2)
print("Go to min")
servo.min()
sleep(2)
print("Go to max")
servo.max()
sleep(2)
print("And back to middle")
servo.mid()
sleep(2)
print("Servo Off")
servo.value = None

print("Now Scan")
while True:
    for i in range(0, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)
