import pytest


@pytest.mark.parametrize("button_value", [True, False])
@pytest.mark.parametrize("button", [0, 1, 2, 3])
def test_read_button(GPIO, sn3218, trilobot, button, button_value):
    bot = trilobot.Trilobot()

    GPIO.input.return_value = button_value
    assert bot.read_button(button) is not button_value
    GPIO.input.assert_called_once()
    GPIO.input.reset_mock()


@pytest.mark.parametrize("button", [4, "monkey", None])
def test_read_button_invalid(GPIO, sn3218, trilobot, button):
    bot = trilobot.Trilobot()

    with pytest.raises((TypeError, ValueError)):
        bot.read_button(button)

    GPIO.input.reset_mock()


@pytest.mark.parametrize("led_value", [0.0, 0.5, 1.0, True, False])
@pytest.mark.parametrize("button_led", [0, 1, 2, 3])
def test_set_button_led(GPIO, sn3218, trilobot, button_led, led_value):
    bot = trilobot.Trilobot()
    bot.set_button_led(button_led, led_value)


@pytest.mark.parametrize("button_led", [4, "monkey", None])
def test_set_button_led_invalid_led(GPIO, sn3218, trilobot, button_led):
    bot = trilobot.Trilobot()

    with pytest.raises((TypeError, ValueError)):
        bot.set_button_led(button_led, 0.5)


@pytest.mark.parametrize("led_value", [-1, 4])
def test_set_button_led_invalid_value(GPIO, sn3218, trilobot, led_value):
    bot = trilobot.Trilobot()

    with pytest.raises((ValueError)):
        bot.set_button_led(0, led_value)
