import pytest


@pytest.mark.parametrize("motor", [0, 1])
@pytest.mark.parametrize("speed", [-1, -0.5, 0, 0.5, 1])
def test_set_motor_speed(GPIO, sn3218, trilobot, motor, speed):
    bot = trilobot.Trilobot()

    bot.set_motor_speed(motor, speed)


@pytest.mark.parametrize("motor", [4, None, "monkey"])
def test_set_motor_speed_invalid(GPIO, sn3218, trilobot, motor):
    bot = trilobot.Trilobot()

    with pytest.raises((TypeError, ValueError)):
        bot.set_motor_speed(motor, 1.0)


@pytest.mark.parametrize("speed", [-1, -0.5, 0, 0.5, 1])
def test_set_motor_speeds(GPIO, sn3218, trilobot, speed):
    bot = trilobot.Trilobot()

    bot.set_motor_speeds(speed, speed)


@pytest.mark.parametrize("speed", [-1, -0.5, 0, 0.5, 1])
def test_set_motor_left_speed(GPIO, sn3218, trilobot, speed):
    bot = trilobot.Trilobot()

    bot.set_left_speed(speed)


@pytest.mark.parametrize("speed", [-1, -0.5, 0, 0.5, 1])
def test_set_motor_right_speed(GPIO, sn3218, trilobot, speed):
    bot = trilobot.Trilobot()

    bot.set_right_speed(speed)


def test_disable_motors(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()

    bot.disable_motors()


@pytest.mark.parametrize("function", [
    "forward",
    "backward",
    "turn_left",
    "turn_right",
    "curve_forward_left",
    "curve_forward_right",
    "curve_backward_left",
    "curve_backward_right",
    "stop",
    "coast",
])
@pytest.mark.parametrize("speed", [-1, -0.5, 0, 0.5, 1])
def test_motor_helpers(GPIO, sn3218, trilobot, function, speed):
    bot = trilobot.Trilobot()
    if function in ("stop", "coast"):
        getattr(bot, function)()
    else:
        getattr(bot, function)(speed)
