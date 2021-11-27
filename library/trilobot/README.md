# Trilobot Library

This is the library for controlling the Trilobot mid-level robot learning platform.


## Getting Started

To start coding your Trilobot, you will need to add the following lines of code to the start of your code file.
```python
from trilobot import *
tbot = Trilobot()
```
This will create a `Trilobot` class called `tbot` that will be used in the rest of the examples going forward.

## Buttons

Trilobot has four buttons to its rear, labelled A, B, X, and Y.
These can be read using the `read_button()` function, which accepts a number between 0 and 3. For convenience, each button can be referred to using these constants.

* `BUTTON_A` = 0
* `BUTTON_B` = 1
* `BUTTON_X` = 2
* `BUTTON_Y` = 3

For example, to read the A button you would write:

```python
state_a = tbot.read_button(BUTTON_A)
```

You can also get the number of buttons using the `NUM_BUTTONS` constant.


## LEDs

Next to each button on Trilobot is a mono LED. These can be controlled using the `set_led()` function, which accepts a number from 0 to 3 (like the buttons), followed by either `True` for On, `False` for Off, or a number between `0.0` and `1.0` for any brightness in between.

For convenience, each LED can be referred to using these constants.
* `LED_A` = 0
* `LED_B` = 1
* `LED_X` = 2
* `LED_Y` = 3

For example, to set the LED next to button B to half brightness you would write:

```python
tbot.set_led(LED_B, 0.5)
```

You can also get the number of LEDs using the `NUM_LEDS` constant.


## Motors

Tribot features two motors with indepentent control, enabling [differential steering](https://en.wikipedia.org/wiki/Differential_steering), whereby the speed of one motor can be controlled independently of the other.

There are several ways these motors can be commanded from code:

### Simple Movements

* `forward()`
* `backward()`
* `turn_left()`
* `turn_right()`
* `curve_forward_left()`
* `curve_forward_right()`
* `curve_backward_left()`
* `curve_backward_right()`

Each of the above functions will drive Trilobot at full speed. To slow the robot down, include a number between `0.0` and `1.0` within the brackets. For example `forward(0.5)` will drive forward at half speed.

To stop Trilobot from moving, simply call `stop()`. This will make the robot stop sharply. If a more gradual stop is wanted, call `coast()` instead.

### Advanced Movements

To get more control over Trilobot's movements, each motor can be individually controlled using `set_left_speed()` or `set_right_speed()`. These take a number between `-1.0` and `1.0`, where positive values will drive the motor forward and negative values will drive the motor backward. The below example will have Trilobot curving slowly to the right.

```python
tbot.set_left_speed(1.0)
tbot.set_right_speed(0.5)
```

If the speeds of both motors are regularly set together, then this can be shortened to a single call to `set_motor_speeds()`. This simplifies the curving right example to:

```python
tbot.set_motor_speeds(1.0, 0.5)
```

A final way the motors can be controlled is by using `set_motor_speed()`, which accepts a number from 0 to 1, followed by a number between `-1.0` and `1.0`.

For convenience, each motor can be referred to using these constants.
* `MOTOR_LEFT` = 0
* `MOTOR_RIGHT` = 1

For example, to set the left motor to half forward speed you would write:

```python
tbot.set_motor_speed(MOTOR_LEFT, 0.5)
```

You can also get the number of motors using the `NUM_MOTORS` constant.

To disable the motors, call `disable_motors()`. This stops their signals and disables the motor driver. Setting any motor speed will enable the driver again.


## Underlighting

One of the funnest features to play with of Trilobot is the six-zone RGB underlighting.

There are several ways these lights can be commanded from code:

### Single Light

A single underlight can be controlled using either `set_underlight()`, which all accept a number from 0 to 5, followed by the colour either as separate red, green, and blue values between `0` and `255`, a list/tuple of three numbers, or a hex colour code. Similarly `set_underlight_hsv()` lets you provide a colour as hue, saturation, and value numbers between `0.0` and `1.0`, and `clear_underlight()` sets the colour to zero.

For convenience, each light can be referred to using these constants.
* `LIGHT_FRONT_RIGHT` = 0
* `LIGHT_FRONT_LEFT` = 1
* `LIGHT_MIDDLE_LEFT` = 2
* `LIGHT_REAR_LEFT` = 3
* `LIGHT_REAR_RIGHT` = 4
* `LIGHT_MIDDLE_RIGHT` = 5

As an example, here are several individual lights being set in various ways:

```python
tbot.set_underlight(LIGHT_FRONT_LEFT, 0, 255, 0)  # Green
tbot.set_underlight(LIGHT_FRONT_RIGHT, '#0000ff')  # Blue
tbot.set_underlight_hsv(LIGHT_REAR_LEFT, 0.0, 1.0, 1.0)  # Red
tbot.clear_underlight(LIGHT_REAR_RIGHT)  # Off
```

### Group Commands

To make some animations easier to create, there are several conveniece functions that will set several underlights to the same colour at the same time.

#### All
* `fill_underlighting()`
* `fill_underlighting_hsv()`
* `clear_underlighting()`

#### Sides
* `set_left_underlights()`
* `set_right_underlights()`
* `set_left_underlights_hsv()`
* `set_right_underlights_hsv()`
* `clear_left_underlights()`
* `clear_right_underlights()`

#### Sections
* `set_front_underlights()`
* `set_middle_underlights()`
* `set_rear_underlights()`
* `set_front_underlights_hsv()`
* `set_middle_underlights_hsv()`
* `set_rear_underlights_hsv()`
* `clear_front_underlights()`
* `clear_middle_underlights()`
* `clear_rear_underlights()`

### Advanced Control

By default all underlight functions will apply the colour to the underlight(s) it is for immediately. This is because they all have an optional `show` parameter that is `True` by default.

For some effects this behaviour may not be wanted, so including `show=False` then calling the function will delay the applying of the colour to the LEDs until the next function that has `show=True`, or `show_underlighting()` can be called explicitly.

In the example below, each light is set to red in a loop, then they are all shown with the end call to `show_underlighting()`:
```python
for led in range(NUM_UNDERLIGHTS):
    tbot.set_underlight(led, 255, 0, 0, show=False)  # Red
     
tbot.show_underlighting()
```

## Distance Sensor

Trilobot features a front mounted ultrasonic distance sensor. This sensor can be read using the `read_distance()` function, which will return a measured distance in centrimetres.

Some default values are used to get these readings, which can be overwritten with the following parameters:

* `timeout`: the total time in milliseconds to try to get distance reading
* `samples`: how many readings to take before returning an average
* `offset`: the time in nanosections the measurement takes (prevents over estimates)

The default `offset` is set to a value that is suitable for the Raspberry Pi 4, but may need adjusting if you are using a different model of Raspberry Pi.

To give more stable readings, this method will attempt to take several readings and return the average distance. You can set the maximum time you want it to take before returning a result so you have control over how long this method ties up your program. It takes as many readings up to the requested number of samples set as it can before the timeout total is reached. It then returns the average distance measured. Any readings where the single reading takes more than the timeout is ignored so these do not distort the average distance measured. 

If no valid readings are taken before the timeout then it returns zero. You can choose parameters to get faster but less accurate readings or take longer to get more samples to average before it returns. The timeout effectively limits the maximum distance the sensor can measure because if the sound pulse takes longer to return over the distance than the timeout set then this method returns zero rather than waiting. So to extend the distance that can be measured, use a larger timeout.

## Servo 

Trilobot features a servo connector between the two motors that can be used to power a small 5V servo.

The following methods are available from code:

* `set_servo_value(value)`: Sets the servo position to a value between `-1.0` and `+1.0`
* `set_servo_angle(angle)`: Sets the servo to an angle in degrees
* `disable_servo()`: Disables the servo, stopping it from running or holding its position
* `servo_to_center()`: Moves the servo to its center
* `servo_to_min()`: Moves the servo to its minimum position
* `servo_to_max()`: Moves the servo to its maximum position
* `servo_to_percent(value, value_min=0, value_max=1, angle_min=-90, angle_max=+90)`: Moves the servo to a position that is a percentage between the minimum and maximum angles specified.

* `initialise_servo(min_angle=-90, max_angle=90, min_pulse_us=500, max_pulse_us=2500)`: Initialises servo control. This gets called automatically when using any of the above functions (other than `disable_servo()`) with default parameters. Calling this from code before that lets you adjust the exact pulse timings that correspond with the minimum and maximum angles your servo is able to reach.