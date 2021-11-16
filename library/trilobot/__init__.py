#!/usr/bin/env python3

import time
import sn3218
import RPi.GPIO as GPIO
from colorsys import hsv_to_rgb

__version__ = '0.0.1'


class Trilobot():
    # User buttons
    BUTTON_A = 5
    BUTTON_B = 6
    BUTTON_X = 16
    BUTTON_Y = 24

    # Onboard LEDs next to each button
    LED_A = 23
    LED_B = 22
    LED_X = 17
    LED_Y = 27

    # Motor, via DRV8833PWP Dual H-Bridge
    MOTOR_EN = 26
    MOTOR_LEFT_P = 11
    MOTOR_LEFT_N = 8
    MOTOR_RIGHT_P = 9
    MOTOR_RIGHT_N = 10

    # HC-SR04 Ultrasound
    ULTRA_TRIG = 13
    ULTRA_ECHO = 25

    # Servo / WS2812
    SERVO = 12

    # SN3218 LED Driver
    UNDERLIGHTING_EN = 7

    # Underlighting LED locations
    FRONT_RIGHT = 0
    FRONT_LEFT = 1
    MIDDLE_LEFT = 2
    REAR_LEFT = 3
    REAR_RIGHT = 4
    MIDDLE_RIGHT = 5
    NUM_UNDERLIGHTS = 6

    # Motor names
    LEFT_MOTOR = 0
    RIGHT_MOTOR = 1
    NUM_MOTORS = 2

    # Half the speed of sound in cm/ns.
    SOUND_CONVERSION_FACTOR_CM_NS = 0.00001715


    def __init__(self):
        """Initialise trilobot
        """

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Setup user buttons
        GPIO.setup(self.BUTTON_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_X, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_Y, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Setup user LEDs
        GPIO.setup(self.LED_A, GPIO.OUT)
        GPIO.setup(self.LED_B, GPIO.OUT)
        GPIO.setup(self.LED_X, GPIO.OUT)
        GPIO.setup(self.LED_Y, GPIO.OUT)

        led_a_pwm = GPIO.PWM(self.LED_A, 2000)
        led_a_pwm.start(0)

        led_b_pwm = GPIO.PWM(self.LED_B, 2000)
        led_b_pwm.start(0)

        led_x_pwm = GPIO.PWM(self.LED_X, 2000)
        led_x_pwm.start(0)

        led_y_pwm = GPIO.PWM(self.LED_Y, 2000)
        led_y_pwm.start(0)
        self.led_pwm_mapping = {self.LED_A: led_a_pwm,
                                self.LED_B: led_b_pwm,
                                self.LED_X: led_x_pwm,
                                self.LED_Y: led_y_pwm}

        # Setup motor driver
        GPIO.setup(self.MOTOR_EN, GPIO.OUT)
        GPIO.setup(self.MOTOR_LEFT_P, GPIO.OUT)
        GPIO.setup(self.MOTOR_LEFT_N, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_P, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_N, GPIO.OUT)

        motor_left_p_pwm = GPIO.PWM(self.MOTOR_LEFT_P, 100)
        motor_left_p_pwm.start(0)

        motor_left_n_pwm = GPIO.PWM(self.MOTOR_LEFT_N, 100)
        motor_left_n_pwm.start(0)

        motor_right_p_pwm = GPIO.PWM(self.MOTOR_RIGHT_P, 100)
        motor_right_p_pwm.start(0)

        motor_right_n_pwm = GPIO.PWM(self.MOTOR_RIGHT_N, 100)
        motor_right_n_pwm.start(0)
        self.motor_pwm_mapping = {self.MOTOR_LEFT_P: motor_left_p_pwm,
                                  self.MOTOR_LEFT_N: motor_left_n_pwm,
                                  self.MOTOR_RIGHT_P: motor_right_p_pwm,
                                  self.MOTOR_RIGHT_N: motor_right_n_pwm}

        GPIO.setup(self.UNDERLIGHTING_EN, GPIO.OUT)
        GPIO.output(self.UNDERLIGHTING_EN, False)

        sn3218.reset()

        sn3218.output([0 for i in range(18)])
        sn3218.enable_leds(0b111111111111111111)
        sn3218.enable()

        self.underlight = [0 for i in range(18)]

        GPIO.output(self.UNDERLIGHTING_EN, False)
        sn3218.output([128 for i in range(18)])

        # setup ultrasonic sensor pins
        GPIO.setup(self.ULTRA_TRIG, GPIO.OUT)
        GPIO.setup(self.ULTRA_ECHO, GPIO.IN)

    def __del__(self):
        sn3218.disable()
        GPIO.cleanup()

    def set_led(self, pin, value):
        pwm = self.led_pwm_mapping[pin]
        if isinstance(value, bool):
            if value:
                pwm.ChangeDutyCycle(100)
            else:
                pwm.ChangeDutyCycle(0)
        elif value < 0.0 or value > 1.0:
            raise ValueError("value must be in the range 0.0 to 1.0")
        else:
            pwm.ChangeDutyCycle(value * 100)

    def read_button(self, pin):
        return not GPIO.input(pin)

    def set_underlighting(self, led, r=0, g=0, b=0):
        if type(led) is not int:
            raise TypeError("led must be an integer")

        if led not in range(self.NUM_UNDERLIGHTS):
            raise ValueError("led must be an integer in the range 0 to 5")

        if r < 0.0 or r > 1.0:
            raise ValueError("r must be in the range 0.0 to 1.0")

        if g < 0.0 or g > 1.0:
            raise ValueError("g must be in the range 0.0 to 1.0")

        if b < 0.0 or b > 1.0:
            raise ValueError("b must be in the range 0.0 to 1.0")

        self.underlight[(led * 3)] = int(r * 255)
        self.underlight[(led * 3) + 1] = int(g * 255)
        self.underlight[(led * 3) + 2] = int(b * 255)

    def show_underlighting(self):
        sn3218.output(self.underlight)
        GPIO.output(self.UNDERLIGHTING_EN, True)

    def fill_underlighting(self, r=0, g=0, b=0):
        if r < 0.0 or r > 1.0:
            raise ValueError("r must be in the range 0.0 to 1.0")

        if g < 0.0 or g > 1.0:
            raise ValueError("g must be in the range 0.0 to 1.0")

        if b < 0.0 or b > 1.0:
            raise ValueError("b must be in the range 0.0 to 1.0")

        for led in range(self.NUM_UNDERLIGHTS):
            self.underlight[(led * 3)] = int(r * 255)
            self.underlight[(led * 3) + 1] = int(g * 255)
            self.underlight[(led * 3) + 2] = int(b * 255)

    def disable_motors(self):
        GPIO.output(self.MOTOR_EN, False)
        self.motor_pwm_mapping[self.MOTOR_LEFT_P].ChangeDutyCycle(0)
        self.motor_pwm_mapping[self.MOTOR_LEFT_N].ChangeDutyCycle(0)
        self.motor_pwm_mapping[self.MOTOR_RIGHT_P].ChangeDutyCycle(0)
        self.motor_pwm_mapping[self.MOTOR_RIGHT_N].ChangeDutyCycle(0)

    def set_motor_speed(self, motor, speed):
        if type(motor) is not int:
            raise TypeError("motor must be an integer")

        if motor not in range(2):
            raise ValueError("motor must be an integer in the range 0 to 1")

        #Limit the speed value rather than throw a value exception
        if speed < -1.0:
            speed = -1.0
        elif speed > 1.0:
            speed = 1.0

        GPIO.output(self.MOTOR_EN, True)
        pwm_p = None
        pwm_n = None
        if motor == 0:
            pwm_p = self.motor_pwm_mapping[self.MOTOR_LEFT_P]
            pwm_n = self.motor_pwm_mapping[self.MOTOR_LEFT_N]
        else:
            # Right motor inverted so a positive speed drives forward
            pwm_p = self.motor_pwm_mapping[self.MOTOR_RIGHT_N]
            pwm_n = self.motor_pwm_mapping[self.MOTOR_RIGHT_P]

        if speed > 0.0:
            pwm_p.ChangeDutyCycle(100)
            pwm_n.ChangeDutyCycle(100 - (speed * 100))
        elif speed < 0.0:
            pwm_p.ChangeDutyCycle(100 - (-speed * 100))
            pwm_n.ChangeDutyCycle(100)
        else:
            pwm_p.ChangeDutyCycle(100)
            pwm_n.ChangeDutyCycle(100)

    def set_left_speed(self, speed):
        self.set_motor_speed(self.LEFT_MOTOR, speed)

    def set_right_speed(self, speed):
        self.set_motor_speed(self.RIGHT_MOTOR, speed)

    def read_distance(self, timeout=50, samples=3, offset=190000):
        """ Return a distance in cm from the ultrasound sensor.
        timeout: total time in ms to try to get distance reading
        samples: determines how many readings to average
        offset: Time in ns the measurement takes (prevents over estimates)
        Returns the measured distance in centimetres as a float.
        
        To give more stable readings, this method will attempt to take several 
        readings and return the average distance. You can set the maximum time 
        you want it to take before returning a result so you have control over 
        how long this method ties up your program. It takes as many readings
        up to the requested number of samples set as it can before the timeout 
        total is reached. It then returns the average distance measured. Any 
        readings where the single reading takes more than the timeout is 
        ignored so these do not distort the average distance measured. If no 
        valid readings are taken before the timeout then it returns zero.

        You can choose parameters to get faster but less accurate readings or 
        take longer to get more samples to average before it returns. The 
        timeout effectively limits the maximum distance the sensor can measure 
        because if the sound pusle takes longer to return over the distance 
        than the timeout set then this method returns zero rather than waiting. 
        So to extend the distance that can be measured, use a larger timeout.
        """

        # Start timing
        start_time = time.perf_counter_ns()
        time_elapsed = 0
        count = 0 # Track now many samples taken
        distance = 0
        average_distance = -999

        # Loop until the timeout is exceeded or all samples have been taken
        while (count < samples) and (time_elapsed < timeout * 1000000):
            # Trigger
            GPIO.output(self.ULTRA_TRIG, 1)
            time.sleep(.00001) # 10 microseconds
            GPIO.output(self.ULTRA_TRIG, 0)

            # Wait for the ECHO pin to go high
            # wait for the pulse rise
            GPIO.wait_for_edge(self.ULTRA_ECHO, GPIO.RISING, timeout=timeout)
            pulse_start = time.perf_counter_ns()

            # And wait for it to fall
            GPIO.wait_for_edge(self.ULTRA_ECHO, GPIO.FALLING, timeout=timeout)
            pulse_end = time.perf_counter_ns()

            # get the duration
            pulse_duration = pulse_end - pulse_start - offset
            if pulse_duration < 0:
                pulse_duration = 0 #Prevent negative readings when offset was too high

            # Only count reading if achieved in less than timeout total time
            if pulse_duration < timeout * 1000000:
                # Convert to distance and add to total
                distance += pulse_duration * self.SOUND_CONVERSION_FACTOR_CM_NS
                count += 1

            time_elapsed = time.perf_counter_ns()-start_time
        
        # Calculate average distance in cm if any successful reading were made
        if count > 0:
            average_distance = distance/count
        
        return average_distance


if __name__ == "__main__":
    trilobot = Trilobot()

    print("Trilobot Function Test")

    time.sleep(2.0)
    for i in range(0, 10):
        print(i)
        GPIO.output(trilobot.UNDERLIGHTING_EN, True)
        time.sleep(0.1)
        GPIO.output(trilobot.UNDERLIGHTING_EN, False)
        time.sleep(0.1)

    for led in range(trilobot.NUM_UNDERLIGHTS):
        trilobot.fill_underlighting(0, 0, 0)
        trilobot.set_underlighting(led, 1.0, 0, 0)
        trilobot.show_underlighting()
        time.sleep(0.1)
        trilobot.fill_underlighting(0, 0, 0)
        trilobot.set_underlighting(led, 0, 1.0, 0)
        trilobot.show_underlighting()
        time.sleep(0.1)
        trilobot.fill_underlighting(0, 0, 0)
        trilobot.set_underlighting(led, 0, 0, 1.0)
        trilobot.show_underlighting()
        time.sleep(0.1)

    trilobot.fill_underlighting(0, 0, 0)
    trilobot.show_underlighting()

    h = 0
    v = 0
    spacing = 1.0 / trilobot.NUM_UNDERLIGHTS

    a = 0
    b = 0
    x = 0
    y = 0
    while True:
        for led in range(trilobot.NUM_UNDERLIGHTS):
            led_h = h + (led * spacing)
            if led_h >= 1.0:
                led_h -= 1.0
            colour = hsv_to_rgb(led_h, 1, 1)
            trilobot.set_underlighting(led, colour[0], colour[1], colour[2])

        trilobot.show_underlighting()
        h += 0.5 / 360
        if h >= 1.0:
            h -= 1.0

        if trilobot.read_button(trilobot.BUTTON_A):
            a = min(a + 0.01, 1.0)
        else:
            a = max(a - 0.01, 0.0)
        trilobot.set_led(trilobot.LED_A, a)

        if trilobot.read_button(trilobot.BUTTON_B):
            b = min(b + 0.01, 1.0)
        else:
            b = max(b - 0.01, 0.0)
        trilobot.set_led(trilobot.LED_B, b)

        if trilobot.read_button(trilobot.BUTTON_X):
            x = min(x + 0.01, 1.0)
        else:
            x = max(x - 0.01, 0.0)
        trilobot.set_led(trilobot.LED_X, x)

        if trilobot.read_button(trilobot.BUTTON_Y):
            y = min(y + 0.01, 1.0)
        else:
            y = max(y - 0.01, 0.0)
        trilobot.set_led(trilobot.LED_Y, y)

        trilobot.set_left_speed(a - b)
        trilobot.set_right_speed(x - y)
        time.sleep(0.01)
