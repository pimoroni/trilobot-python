#!/usr/bin/env python3

import time
import sn3218
import RPi.GPIO as GPIO
from colorsys import hsv_to_rgb

__version__ = '0.0.2'

BUTTON_A = 0
BUTTON_B = 1
BUTTON_X = 2
BUTTON_Y = 3
NUM_BUTTONS = 4

# Underlighting LED locations
LIGHT_FRONT_RIGHT = 0
LIGHT_FRONT_LEFT = 1
LIGHT_MIDDLE_LEFT = 2
LIGHT_REAR_LEFT = 3
LIGHT_REAR_RIGHT = 4
LIGHT_MIDDLE_RIGHT = 5
NUM_UNDERLIGHTS = 6

# Useful underlighting groups
LIGHTS_LEFT = (LIGHT_FRONT_LEFT, LIGHT_MIDDLE_LEFT, LIGHT_REAR_LEFT)
LIGHTS_RIGHT = (LIGHT_FRONT_RIGHT, LIGHT_MIDDLE_RIGHT, LIGHT_REAR_RIGHT)
LIGHTS_FRONT = (LIGHT_FRONT_LEFT, LIGHT_FRONT_RIGHT)
LIGHTS_MIDDLE = (LIGHT_MIDDLE_LEFT, LIGHT_MIDDLE_RIGHT)
LIGHTS_REAR = (LIGHT_REAR_LEFT, LIGHT_REAR_RIGHT)
LIGHTS_LEFT_DIAGONAL = (LIGHT_FRONT_LEFT, LIGHT_REAR_RIGHT)
LIGHTS_RIGHT_DIAGONAL = (LIGHT_FRONT_RIGHT, LIGHT_REAR_LEFT)

# Motor names
MOTOR_LEFT = 0
MOTOR_RIGHT = 1
NUM_MOTORS = 2


class Trilobot():
    # User button pins
    BUTTON_A_PIN = 5
    BUTTON_B_PIN = 6
    BUTTON_X_PIN = 16
    BUTTON_Y_PIN = 24

    # Onboard LEDs pins (next to each button)
    LED_A_PIN = 23
    LED_B_PIN = 22
    LED_X_PIN = 17
    LED_Y_PIN = 27

    # Motor driver pins, via DRV8833PWP Dual H-Bridge
    MOTOR_EN_PIN = 26
    MOTOR_LEFT_P = 8
    MOTOR_LEFT_N = 11
    MOTOR_RIGHT_P = 10
    MOTOR_RIGHT_N = 9

    # HC-SR04 Ultrasound pins
    ULTRA_TRIG_PIN = 13
    ULTRA_ECHO_PIN = 25

    # Servo / WS2812 pin
    SERVO_PIN = 12

    # SN3218 LED Driver pin
    UNDERLIGHTING_EN_PIN = 7

    # Speed of sound is 343m/s which we need in cm/ns for our distance measure
    SPEED_OF_SOUND_CM_NS = 343 * 100 / 1E9  # 0.0000343 cm / ns

    def __init__(self):
        """ Initialise trilobot's hardware functions
        """

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Setup user buttons
        GPIO.setup(self.BUTTON_A_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_X_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_Y_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.buttons = (self.BUTTON_A_PIN, self.BUTTON_B_PIN, self.BUTTON_X_PIN, self.BUTTON_Y_PIN)

        # Setup user LEDs
        GPIO.setup(self.LED_A_PIN, GPIO.OUT)
        GPIO.setup(self.LED_B_PIN, GPIO.OUT)
        GPIO.setup(self.LED_X_PIN, GPIO.OUT)
        GPIO.setup(self.LED_Y_PIN, GPIO.OUT)
        self.leds = (self.LED_A_PIN, self.LED_B_PIN, self.LED_X_PIN, self.LED_Y_PIN)

        led_a_pwm = GPIO.PWM(self.LED_A_PIN, 2000)
        led_a_pwm.start(0)

        led_b_pwm = GPIO.PWM(self.LED_B_PIN, 2000)
        led_b_pwm.start(0)

        led_x_pwm = GPIO.PWM(self.LED_X_PIN, 2000)
        led_x_pwm.start(0)

        led_y_pwm = GPIO.PWM(self.LED_Y_PIN, 2000)
        led_y_pwm.start(0)
        self.led_pwm_mapping = {self.LED_A_PIN: led_a_pwm,
                                self.LED_B_PIN: led_b_pwm,
                                self.LED_X_PIN: led_x_pwm,
                                self.LED_Y_PIN: led_y_pwm}

        # Setup motor driver
        GPIO.setup(self.MOTOR_EN_PIN, GPIO.OUT)
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

        try:
            self.sn3218 = sn3218.SN3218()
        except NameError:
            self.sn3218 = sn3218

        self.sn3218.reset()

        self.underlight = [0 for i in range(18)]
        self.sn3218.output(self.underlight)
        self.sn3218.enable_leds(0b111111111111111111)
        self.sn3218.disable()

        # setup ultrasonic sensor pins
        GPIO.setup(self.ULTRA_TRIG_PIN, GPIO.OUT)
        GPIO.setup(self.ULTRA_ECHO_PIN, GPIO.IN)

        # setup the servo object to None, for later initialisation
        self.servo = None

    def __del__(self):
        """ Clean up GPIO and underlighting when the class is deleted.
        """
        self.sn3218.disable()
        GPIO.cleanup()

    ###########
    # Buttons #
    ###########
    def read_button(self, button):
        """ Return whether or not a given button is pressed.
        button: the ID of the button to read the state of
        Returns True for pressed, False for released
        """
        if type(button) is not int:
            raise TypeError("button must be an integer")

        if button not in range(NUM_BUTTONS):
            raise ValueError("""button must be an integer in the range 0 to 3. For convenience, use the constants:
                BUTTON_A (0), BUTTON_B (1), BUTTON_X (2), or BUTTON_Y (3)""")

        return not GPIO.input(self.buttons[button])

    ########
    # LEDs #
    ########
    def set_button_led(self, button_led, value):
        """ Turns the given button LED on or off, or to a brighness value.
        button_led: the ID of the button LED to set the state of
        value: either True for on, False for off, or a number between 0.0 and 1.0
        """
        if type(button_led) is not int:
            raise TypeError("led must be an integer")

        if button_led not in range(NUM_BUTTONS):
            raise ValueError("""button_led must be an integer in the range 0 to 3. For convenience, use the constants:
                BUTTON_A (0), BUTTON_B (1), BUTTON_X (2), or BUTTON_Y (3)""")

        pwm = self.led_pwm_mapping[self.leds[button_led]]
        if isinstance(value, bool):
            if value:
                pwm.ChangeDutyCycle(100)
            else:
                pwm.ChangeDutyCycle(0)
        elif value < 0.0 or value > 1.0:
            raise ValueError("value must be in the range 0.0 to 1.0")
        else:
            pwm.ChangeDutyCycle(value * 100)

    ##########
    # Motors #
    ##########
    def set_motor_speed(self, motor, speed):
        """ Sets the speed of the given motor.
        motor: the ID of the motor to set the state of
        speed: the motor speed, between -1.0 and 1.0
        """
        if type(motor) is not int:
            raise TypeError("motor must be an integer")

        if motor not in range(2):
            raise ValueError("""motor must be an integer in the range 0 to 1. For convenience, use the constants:
                MOTOR_LEFT (0), or MOTOR_RIGHT (1)""")

        # Limit the speed value rather than throw a value exception
        speed = max(min(speed, 1.0), -1.0)

        GPIO.output(self.MOTOR_EN_PIN, True)
        pwm_p = None
        pwm_n = None
        if motor == 0:
            # Left motor inverted so a positive speed drives forward
            pwm_p = self.motor_pwm_mapping[self.MOTOR_LEFT_N]
            pwm_n = self.motor_pwm_mapping[self.MOTOR_LEFT_P]
        else:
            pwm_p = self.motor_pwm_mapping[self.MOTOR_RIGHT_P]
            pwm_n = self.motor_pwm_mapping[self.MOTOR_RIGHT_N]

        if speed > 0.0:
            pwm_p.ChangeDutyCycle(100)
            pwm_n.ChangeDutyCycle(100 - (speed * 100))
        elif speed < 0.0:
            pwm_p.ChangeDutyCycle(100 - (-speed * 100))
            pwm_n.ChangeDutyCycle(100)
        else:
            pwm_p.ChangeDutyCycle(100)
            pwm_n.ChangeDutyCycle(100)

    def set_motor_speeds(self, l_speed, r_speed):
        """ Sets the speeds of both motors at once.
        l_speed: the left motor speed, between -1.0 and 1.0
        r_speed: the right motor speed, between -1.0 and 1.0
        """
        self.set_motor_speed(MOTOR_LEFT, l_speed)
        self.set_motor_speed(MOTOR_RIGHT, r_speed)

    def set_left_speed(self, speed):
        """ Sets the speed of the left motor only.
        speed: the speed, between -1.0 and 1.0
        """
        self.set_motor_speed(MOTOR_LEFT, speed)

    def set_right_speed(self, speed):
        """ Sets the speed of the right motor only.
        speed: the speed, between -1.0 and 1.0
        """
        self.set_motor_speed(MOTOR_RIGHT, speed)

    def disable_motors(self):
        """ Disables both motors, allowing them to spin freely.
        """
        GPIO.output(self.MOTOR_EN_PIN, False)
        self.motor_pwm_mapping[self.MOTOR_LEFT_P].ChangeDutyCycle(0)
        self.motor_pwm_mapping[self.MOTOR_LEFT_N].ChangeDutyCycle(0)
        self.motor_pwm_mapping[self.MOTOR_RIGHT_P].ChangeDutyCycle(0)
        self.motor_pwm_mapping[self.MOTOR_RIGHT_N].ChangeDutyCycle(0)

    #################
    # Motor Helpers #
    #################
    def forward(self, speed=1.0):
        """ Drives Trilobot forward.
        speed: the speed to drive at, between 0.0 and 1.0
        """
        self.set_motor_speeds(speed, speed)

    def backward(self, speed=1.0):
        """ Drives Trilobot backward.
        speed: the speed to drive at, between 0.0 and 1.0
        """
        self.set_motor_speeds(-speed, -speed)

    def turn_left(self, speed=1.0):
        """ Turns Trilobot left.
        speed: the speed to turn at, between 0.0 and 1.0
        """
        self.set_motor_speeds(-speed, speed)

    def turn_right(self, speed=1.0):
        """ Turns Trilobot right.
        speed: the speed to turn at, between 0.0 and 1.0
        """
        self.set_motor_speeds(speed, -speed)

    def curve_forward_left(self, speed=1.0):
        """ Drives Trilobot forward and to the left.
        speed: the speed to drive at, between 0.0 and 1.0
        """
        self.set_motor_speeds(0.0, speed)

    def curve_forward_right(self, speed=1.0):
        """ Drives Trilobot forward and to the right.
        speed: the speed to drive at, between 0.0 and 1.0
        """
        self.set_motor_speeds(speed, 0.0)

    def curve_backward_left(self, speed=1.0):
        """ Drives Trilobot backward and to the left.
        speed: the speed to drive at, between 0.0 and 1.0
        """
        self.set_motor_speeds(0.0, -speed)

    def curve_backward_right(self, speed=1.0):
        """ Drives Trilobot backward and to the right.
        speed: the speed to drive at, between 0.0 and 1.0
        """
        self.set_motor_speeds(-speed, 0.0)

    def stop(self):
        """ Stops Trilobot from driving, sharply.
        """
        self.set_motor_speeds(0.0, 0.0)

    def coast(self):
        """ Stops Trilobot from driving, slowly.
        """
        self.disable_motors()

    #################
    # Underlighting #
    #################
    def show_underlighting(self):
        """ Shows the previously stored colors on Trilobot's underlights.
        """
        self.sn3218.output(self.underlight)
        self.sn3218.enable()

    def disable_underlighting(self):
        """ Disables Trilobot's underlighting, preserving the last set colors.
        """
        self.sn3218.disable()

    def set_underlight(self, light, r_color, g=None, b=None, show=True):
        """ Sets a single underlight to a given RGB color.
        light: the ID of the light to set the color of
        r_color: the red component of the color (from 0 to 255), or a list/tuple containing all three color components.
        g: the green component of the color (from 0 to 255), if r_color was not given a list/tuple
        b: the blue component of the color (from 0 to 255), if r_color was not given a list/tuple
        show: whether or not to show the new color immediately
        """
        if type(light) is not int:
            raise TypeError("light must be an integer")

        if light not in range(NUM_UNDERLIGHTS):
            raise ValueError("""light must be an integer in the range 0 to 5. For convenience, use the constants:
                LIGHT_FRONT_RIGHT (0), LIGHT_FRONT_LEFT (1), LIGHT_MIDDLE_LEFT (2), LIGHT_REAR_LEFT (3), LIGHT_REAR_RIGHT (4), or LIGHT_MIDDLE_RIGHT (5)""")

        if g is None and b is None:
            # Treat r_color as a colour

            if isinstance(r_color, str):
                value = r_color.strip('#')
                r_color = list(int(value[i:i + 2], 16) for i in (0, 2, 4))

            if isinstance(r_color, list) or isinstance(r_color, tuple):
                if len(r_color) != 3 or \
                        (r_color[0] < 0 or r_color[0] > 255) or \
                        (r_color[1] < 0 or r_color[1] > 255) or \
                        (r_color[2] < 0 or r_color[2] > 255):
                    raise ValueError("color must either be a color hex code, or a list/tuple of 3 numbers between 0 and 255")

                self.underlight[(light * 3)] = int(r_color[0])
                self.underlight[(light * 3) + 1] = int(r_color[1])
                self.underlight[(light * 3) + 2] = int(r_color[2])
            else:
                raise ValueError("color must either be a color hex code, or a list/tuple of 3 numbers between 0 and 255")

        else:
            if r_color < 0 or r_color > 255:
                raise ValueError("r must be in the range 0 to 255")

            if g is None or g < 0 or g > 255:
                raise ValueError("g must be in the range 0 to 255")

            if b is None or b < 0 or b > 255:
                raise ValueError("b must be in the range 0 to 255")

            self.underlight[(light * 3)] = int(r_color)
            self.underlight[(light * 3) + 1] = int(g)
            self.underlight[(light * 3) + 2] = int(b)

        if show:
            self.show_underlighting()

    def set_underlight_hsv(self, light, h, s=1, v=1, show=True):
        """ Sets a single underlight to a given HSV color.
        light: the ID of the light to set the color of
        h: the hue of the color (from 0.0 to 1.0)
        s: the saturation of the color (from 0.0 to 1.0)
        v: the value of the color (from 0.0 to 1.0)
        show: whether or not to show the new color immediately
        """
        color = [i * 255 for i in hsv_to_rgb(h, s, v)]
        self.set_underlight(light, color, show=show)

    def fill_underlighting(self, r_color, g=None, b=None, show=True):
        """ Fill all the underlights with a given RGB color.
        light: the ID of the light to set the color of
        r_color: the red component of the color (from 0 to 255), or a list/tuple containing all three color components.
        g: the green component of the color (from 0 to 255), if r_color was not given a list/tuple
        b: the blue component of the color (from 0 to 255), if r_color was not given a list/tuple
        show: whether or not to show the new color immediately
        """
        for i in range(0, NUM_UNDERLIGHTS):
            self.set_underlight(i, r_color, g, b, show=False)
        if show:
            self.show_underlighting()

    def fill_underlighting_hsv(self, h, s=1, v=1, show=True):
        """ Fill all the underlights with a given HSV color.
        h: the hue of the color (from 0.0 to 1.0)
        s: the saturation of the color (from 0.0 to 1.0)
        v: the value of the color (from 0.0 to 1.0)
        show: whether or not to show the new color immediately
        """
        color = [i * 255 for i in hsv_to_rgb(h, s, v)]
        for i in range(0, NUM_UNDERLIGHTS):
            self.set_underlight(i, color, show=False)
        if show:
            self.show_underlighting()

    def clear_underlight(self, light, show=True):
        """ Clear the color of a single underlight. This has the effect of turning it off.
        light: the ID of the light to clear
        show: whether or not to show the new color immediately
        """
        self.set_underlight(light, 0, 0, 0, show=show)

    def clear_underlighting(self, show=True):
        """ Clear the color of all underlights. This has the effect of turning them off.
        show: whether or not to show the new color immediately
        """
        self.fill_underlighting(0, 0, 0, show=show)

    #########################
    # Underlighting Helpers #
    #########################
    def set_underlights(self, lights, r_color, g=None, b=None, show=True):
        """ Sets a group of underlights to a given RGB color.
        lights: a list/tuple containing the IDs of the lights to set the color of
        r_color: the red component of the color (from 0 to 255), or a list/tuple containing all three color components.
        g: the green component of the color (from 0 to 255), if r_color was not given a list/tuple
        b: the blue component of the color (from 0 to 255), if r_color was not given a list/tuple
        show: whether or not to show the new color immediately
        """
        if type(lights) != list and type(lights) != tuple:
            raise TypeError("lights must be a list or tuple containing the numbers for the underlights to set (from 0 to 5)")

        light_count = len(lights)
        if light_count > NUM_UNDERLIGHTS:
            raise ValueError("lights contains more values than the number of underlights available")
        if light_count == 0:
            raise ValueError("lights cannot be empty")

        if light_count > 1:
            for i in range(0, light_count - 1):
                self.set_underlight(lights[i], r_color, g, b, show=False)

        self.set_underlight(lights[light_count - 1], r_color, g, b, show=show)

    def set_underlights_hsv(self, lights, h, s=1, v=1, show=True):
        """ Sets a group of underlights to a single HSV color.
        lights: a list/tuple containing the IDs of the lights to set the color of
        h: the hue of the color (from 0.0 to 1.0)
        s: the saturation of the color (from 0.0 to 1.0)
        v: the value of the color (from 0.0 to 1.0)
        show: whether or not to show the new color immediately
        """
        color = [i * 255 for i in hsv_to_rgb(h, s, v)]
        self.set_underlights(lights, color, show=show)

    def clear_underlights(self, lights, show=True):
        """ Clear the color of a group of underlights. This has the effect of turning them off.
        lights: a list/tuple containing the IDs of the lights to set the color of
        show: whether or not to show the new color immediately
        """
        self.set_underlights(lights, 0, 0, 0, show=show)

    ##############
    # Ultrasound #
    ##############
    def read_distance(self, timeout=50, samples=3, offset=190000):
        """ Return a distance in cm from the ultrasound sensor.
        timeout: total time in ms to try to get distance reading
        samples: determines how many readings to average
        offset: Time in ns the measurement takes (prevents over estimates)
        The default offset here is about right for a Raspberry Pi 4.
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
        count = 0  # Track now many samples taken
        total_pulse_durations = 0
        distance = -999

        # Loop until the timeout is exceeded or all samples have been taken
        while (count < samples) and (time_elapsed < timeout * 1000000):
            # Trigger
            GPIO.output(self.ULTRA_TRIG_PIN, 1)
            time.sleep(.00001)  # 10 microseconds
            GPIO.output(self.ULTRA_TRIG_PIN, 0)

            # Wait for the ECHO pin to go high
            # wait for the pulse rise
            GPIO.wait_for_edge(self.ULTRA_ECHO_PIN, GPIO.RISING, timeout=timeout)
            pulse_start = time.perf_counter_ns()

            # And wait for it to fall
            GPIO.wait_for_edge(self.ULTRA_ECHO_PIN, GPIO.FALLING, timeout=timeout)
            pulse_end = time.perf_counter_ns()

            # get the duration
            pulse_duration = pulse_end - pulse_start - offset
            if pulse_duration < 0:
                pulse_duration = 0  # Prevent negative readings when offset was too high

            # Only count reading if achieved in less than timeout total time
            if pulse_duration < timeout * 1000000:
                # Convert to distance and add to total
                total_pulse_durations += pulse_duration
                count += 1

            time_elapsed = time.perf_counter_ns() - start_time

        # Calculate average distance in cm if any successful reading were made
        if count > 0:
            # Calculate distance using speed of sound divided by number of samples and half
            # that as sound pulse travels from robot to obstacle and back (twice the distance)
            distance = total_pulse_durations * self.SPEED_OF_SOUND_CM_NS / (2 * count)

        return distance

    #########
    # Servo #
    #########
    def initialise_servo(self, min_angle=-90, max_angle=90, min_pulse_us=500, max_pulse_us=2500):
        if self.servo is not None:
            raise RuntimeError("Servo is already initialised.")

        # if not exists /var/run/pigpio.pid:
        #    stop now
        import os
        import sys
        if not os.path.isfile('/var/run/pigpio.pid'):
            print('Trilobot uses pigpio for Servo control.')
            print('If it is not already installed, please install it with "sudo apt install pigpio"')
            print('Then run "sudo pigpiod" to enable it until the next boot, \
and "sudo systemctl enable pigpiod" to have it auto-start on every boot')
            sys.exit()

        # set up servo control
        from gpiozero.pins.pigpio import PiGPIOFactory
        from gpiozero import AngularServo
        self.servo = AngularServo(self.SERVO_PIN, initial_angle=None,
                                  min_angle=min_angle,
                                  max_angle=max_angle,
                                  min_pulse_width=min_pulse_us / 1000000,
                                  max_pulse_width=max_pulse_us / 1000000,
                                  pin_factory=PiGPIOFactory())

    def set_servo_value(self, value):
        """ Sets the servo to a given value between its minimum and maximum angles.
        value: a number between -1.0 and 1.0
        """
        if self.servo is None:
            self.initialise_servo()
        self.servo.value = value

    def set_servo_angle(self, angle):
        """ Sets the servo to a given angle.
        angle: an angle in degrees between -90 and +90
        """
        if self.servo is None:
            self.initialise_servo()
        self.servo.angle = angle

    def disable_servo(self):
        """ Disables the servo, allowing it to be turned freely.
        """
        if self.servo is not None:
            self.servo.value = None

    #########################
    # Servo Helpers #
    #########################
    def servo_to_center(self):
        """ Moves the servo to its center angle.
        """
        if self.servo is None:
            self.initialise_servo()
        self.servo.mid()

    def servo_to_min(self):
        """ Moves the servo to its minimum angle.
        """
        if self.servo is None:
            self.initialise_servo()
        self.servo.min()

    def servo_to_max(self):
        """ Moves the servo to its maximum angle.
        """
        if self.servo is None:
            self.initialise_servo()
        self.servo.max()

    def servo_to_percent(self, value, value_min=0, value_max=1, angle_min=-90, angle_max=+90):
        """ Moves the servo to an angle between the given minimum and maximums.
        Useful for having a sensor that outputs between two values move the servo between two particular angles.
        By default this will convert a percentage value between 0.0 and 1.0 to servo angles of -90 and +90 degrees.
        value: the value to be applied to the servo
        value_min: the minimum value expected
        value_max: the maximum value expected
        angle_min: the angle that corresponds to value_min
        angle_max: the angle that corresponds to value_max
        """
        if self.servo is None:
            self.initialise_servo()
        # Map the value from its range to an angle range
        angle = (value - value_min) * (angle_max - angle_min) / (value_max - value_min) + angle_min
        self.set_servo_angle(angle)


if __name__ == "__main__":
    tbot = Trilobot()

    print("Trilobot Function Test")

    time.sleep(2.0)
    tbot.fill_underlighting(127, 127, 127, show=False)
    for i in range(0, 10):
        print(i)
        tbot.show_underlighting()
        time.sleep(0.1)
        tbot.disable_underlighting()
        time.sleep(0.5)

    for led in range(NUM_UNDERLIGHTS):
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(led, 255, 0, 0)
        time.sleep(0.1)
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(led, 0, 255, 0)
        time.sleep(0.1)
        tbot.clear_underlighting(show=False)
        tbot.set_underlight(led, 0, 0, 255)
        time.sleep(0.1)

    tbot.clear_underlighting()

    h = 0
    v = 0
    spacing = 1.0 / NUM_UNDERLIGHTS

    a = 0
    b = 0
    x = 0
    y = 0
    while True:
        for led in range(NUM_UNDERLIGHTS):
            led_h = h + (led * spacing)
            if led_h >= 1.0:
                led_h -= 1.0
            tbot.set_underlight_hsv(led, led_h, 1, 1, show=False)

        tbot.show_underlighting()
        h += 0.5 / 360
        if h >= 1.0:
            h -= 1.0

        if tbot.read_button(BUTTON_A):
            a = min(a + 0.01, 1.0)
        else:
            a = max(a - 0.01, 0.0)
        tbot.set_button_led(BUTTON_A, a)

        if tbot.read_button(BUTTON_B):
            b = min(b + 0.01, 1.0)
        else:
            b = max(b - 0.01, 0.0)
        tbot.set_button_led(BUTTON_B, b)

        if tbot.read_button(BUTTON_X):
            x = min(x + 0.01, 1.0)
        else:
            x = max(x - 0.01, 0.0)
        tbot.set_button_led(BUTTON_X, x)

        if tbot.read_button(BUTTON_Y):
            y = min(y + 0.01, 1.0)
        else:
            y = max(y - 0.01, 0.0)
        tbot.set_button_led(BUTTON_Y, y)

        tbot.set_left_speed(a - b)
        tbot.set_right_speed(x - y)
        time.sleep(0.01)
