# Trilobot Examples <!-- omit in toc -->

- [Function Examples](#function-examples)
  - [Single Button](#single-button)
  - [Multiple Buttons](#multiple-buttons)
  - [Flash Button LEDs](#flash-button-leds)
  - [Fade Button LEDs](#fade-button-leds)
  - [Print Distance](#print-distance)
- [Motor Examples](#motor-examples)
  - [Movements](#movements)
  - [Follow Straight](#follow-straight)
  - [Avoid Walls](#avoid-walls)
- [Lighting Examples](#lighting-examples)
  - [Flash Underlights](#flash-underlights)
  - [Distance Lights](#distance-lights)
  - [Underlighting Groups](#underlighting-groups)
  - [Show Underlighting](#show-underlighting)
  - [Underlight Chaser](#underlight-chaser)
  - [Underlight Fade Chaser](#underlight-fade-chaser)
- [Servo Examples](#servo-examples)
  - [Servo Control](#servo-control)
  - [Calibrated Servo](#calibrated-servo)
- [Advanced Examples](#advanced-examples)
  - [Remote Control](#remote-control)


## Function Examples

### Single Button
[single_button.py](single_button.py)

Shows how to read one of Trilobots buttons and tell if it was pressed or released.

### Multiple Buttons
[multiple_buttons.py](multiple_buttons.py)

Shows how to read all of Trilobots buttons and tell if they were pressed or released.

### Flash Button LEDs
[flash_button_leds.py](flash_button_leds.py)

Shows how to turn the button LEDs on and off, by having them flash.

### Fade Button LEDs
[fade_button_leds.py](fade_button_leds.py)

Shows how to control the brightness of the button LEDs, by having them fade up and down.

### Reactive Button LEDs
[reactive_button_leds.py](reactive_button_leds.py)

Shows how to use the buttons to make their neighbouring LEDs fade up when pressed and fade down when released.

### Print Distance

[print_distance.py](print_distance.py)

This demonstrates how to read distance values from Trilobot's ultrasound distance sensor. It will print the values it reads onto the console in cm, along with the time taken to get the readings.


## Motor Examples

### Movements
[movements.py](movements.py)

An example of how to perform simple movements of Trilobot.


### Follow Straight
[follow_straight.py](follow_straight.py)

A demonstration of Trilobot's ultrasound sensor that has it keep an object a goal distance in front of it. If the object gets closer Trilobot will reverse, if the object gets further away Trilobot will drive forward.

### Avoid Walls
[avoid_walls.py](avoid_walls.py)

Further demonstrating Trilobot's ultrasound distance sensor, this example will drive forward and then turn right to avoid obstacles it detects them with the sensor.


## Lighting Examples

### Flash Underlights
[flash_underlights.py](flash_underlights.py)

This example will demonstrate the RGB underlights of Trilobot, by making them flash in a red, green and blue sequence.

### Distance Lights
[distance_lights.py](distance_lights.py)

This brings together the underlights and the distance sensor, using the underlights to indicate if something is too close with red, orange, green indications. It also prints distances on the console.

### Underlighting Groups
[underlighting_groups.py](underlighting_groups.py)

Examples of how to set multiple Trilobot underlights to a color with one command.

### Show Underlighting
[show_underlighting.py](show_underlighting.py)

Examples of how to set Trilobot's underlights to different colors and have them all show at the same time.

### Underlight Chaser
[underlight_chaser.py](underlight_chaser.py)

An example chaser animation using Trilobot's underlighting.

### Underlight Fade Chaser
[underlight_fade_chaser.py](underlight_fade_chaser.py)

A smoother chaser animation example on Trilobot's underlights, using fading on each light.


## Servo Examples

### Servo Control

[servo_control.py](servo_control.py)

An example of how to command a servo connected to Trilobot to move and perform sweeping motions.

### Calibrated Servo
[calibrated_servo.py](calibrated_servo.py)

An example of how to set a calibration on a servo connected to Trilobot, and have it move to exact angles.


## Advanced Examples

### Remote Control
[remote_control.py](remote_control.py)

An advanced example of how Trilobot can be remote controlled using a controller or gamepad. This will require one of the supported controllers to already be paired to your Trilobot.

At startup a list of supported controllers will be shown, with you being asked to select one. The program will then attempt to connect to the controller, and if successful Trilobot's underlights will illuminate with a rainbow pattern.

From there you can drive your Trilobot around using the left analog stick or d-pad. Pressing the right trigger will switch to Tank-steer mode, where the left analog stick controls the left wheel, and the right analog stick controls the right wheel. Pressing the left trigger will switch back to regular mode.

If your controller becomes disconnected Trilobot will stop moving and show a slow red pulsing animation on its underlights. Simply reconnect your controller and after 10 to 20 seconds, the program should find your controller again and start up again.

Support for further controllers can be added to [library/trilobot/controller_mappings.py](../library/trilobot/controller_mappings.py)
