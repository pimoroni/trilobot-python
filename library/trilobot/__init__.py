#!/usr/bin/env python3

import time
import sn3218

from colorsys import hsv_to_rgb

import RPi.GPIO as GPIO

__version__ = '0.0.1'


# User buttons
BUTTON_A = 24
BUTTON_B = 16
BUTTON_X = 6
BUTTON_Y = 5

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
FRONT_LEFT = 0
MIDDLE_LEFT = 1
REAR_LEFT = 2
REAR_RIGHT = 3
MIDDLE_RIGHT = 4
FRONT_RIGHT = 5
NUM_UNDERLIGHTS = 6


class Trilobot():
    def __init__(self):
        """Initialise trilobot
        """

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Setup user buttons
        GPIO.setup(BUTTON_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_X, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_Y, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Setup user LEDs
        GPIO.setup(LED_A, GPIO.OUT)
        GPIO.setup(LED_B, GPIO.OUT)
        GPIO.setup(LED_X, GPIO.OUT)
        GPIO.setup(LED_Y, GPIO.OUT)

        led_a_pwm = GPIO.PWM(LED_A, 2000)
        led_a_pwm.start(0)

        led_b_pwm = GPIO.PWM(LED_B, 2000)
        led_b_pwm.start(0)

        led_x_pwm = GPIO.PWM(LED_X, 2000)
        led_x_pwm.start(0)

        led_y_pwm = GPIO.PWM(LED_Y, 2000)
        led_y_pwm.start(0)
        self.led_pwm_mapping = {LED_A: led_a_pwm,
                                LED_B: led_b_pwm,
                                LED_X: led_x_pwm,
                                LED_Y: led_y_pwm}

        # Setup motor driver
        GPIO.setup(MOTOR_EN, GPIO.OUT)
        GPIO.setup(MOTOR_LEFT_P, GPIO.OUT)
        GPIO.setup(MOTOR_LEFT_N, GPIO.OUT)
        GPIO.setup(MOTOR_RIGHT_P, GPIO.OUT)
        GPIO.setup(MOTOR_RIGHT_N, GPIO.OUT)

        GPIO.setup(UNDERLIGHTING_EN, GPIO.OUT)
        GPIO.output(UNDERLIGHTING_EN, False)

        sn3218.reset()

        sn3218.output([0 for i in range(18)])
        sn3218.enable_leds(0b111111111111111111)
        sn3218.enable()

        self.underlight = [0 for i in range(18)]

        GPIO.output(UNDERLIGHTING_EN, False)
        sn3218.output([128 for i in range(18)])

        time.sleep(2.0)
        for i in range(0, 10):
            print(i)
            GPIO.output(UNDERLIGHTING_EN, True)
            time.sleep(0.1)
            GPIO.output(UNDERLIGHTING_EN, False)
            time.sleep(0.1)
        # SPEED_OF_SOUND = 343

        # ultrasound = Echo(ULTRA_TRIG, ULTRA_ECHO, SPEED_OF_SOUND)

        # GPIO.setup(SERVO, GPIO.OUT)
        # servo = GPIO.PWM(SERVO, 50)
        # servo.start(0)

        # GPIO.setup(ULTRA_TRIG, GPIO.OUT)
        # GPIO.setup(ULTRA_ECHO, GPIO.IN)

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

        if led not in range(NUM_UNDERLIGHTS):
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
        GPIO.output(UNDERLIGHTING_EN, True)

    def fill_underlighting(self, r=0, g=0, b=0):
        if r < 0.0 or r > 1.0:
            raise ValueError("r must be in the range 0.0 to 1.0")

        if g < 0.0 or g > 1.0:
            raise ValueError("g must be in the range 0.0 to 1.0")

        if b < 0.0 or b > 1.0:
            raise ValueError("b must be in the range 0.0 to 1.0")

        for led in range(NUM_UNDERLIGHTS):
            self.underlight[(led * 3)] = int(r * 255)
            self.underlight[(led * 3) + 1] = int(g * 255)
            self.underlight[(led * 3) + 2] = int(b * 255)


if __name__ == "__main__":
    trilobot = Trilobot()

    print("Trilobot Function Test")

    for led in range(NUM_UNDERLIGHTS):
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
            colour = hsv_to_rgb(led_h, 1, 1)
            trilobot.set_underlighting(led, colour[0], colour[1], colour[2])

        trilobot.show_underlighting()
        h += 0.5 / 360
        if h >= 1.0:
            h -= 1.0

        if trilobot.read_button(BUTTON_A):
            a = min(a + 0.01, 1.0)
        else:
            a = max(a - 0.01, 0.0)
        trilobot.set_led(LED_A, a)

        if trilobot.read_button(BUTTON_B):
            b = min(b + 0.01, 1.0)
        else:
            b = max(b - 0.01, 0.0)
        trilobot.set_led(LED_B, b)

        if trilobot.read_button(BUTTON_X):
            x = min(x + 0.01, 1.0)
        else:
            x = max(x - 0.01, 0.0)
        trilobot.set_led(LED_X, x)

        if trilobot.read_button(BUTTON_Y):
            y = min(y + 0.01, 1.0)
        else:
            y = max(y - 0.01, 0.0)
        trilobot.set_led(LED_Y, y)

        # trilobot.set_led(LED_A, trilobot.read_button(BUTTON_A))
        # trilobot.set_led(LED_B, trilobot.read_button(BUTTON_B))
        # trilobot.set_led(LED_X, trilobot.read_button(BUTTON_X))
        # trilobot.set_led(LED_Y, trilobot.read_button(BUTTON_Y))
        time.sleep(0.01)
