import pytest


def test_show_underlighting(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.show_underlighting()


def test_disable_underlighting(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.disable_underlighting()


@pytest.mark.parametrize("show", [True, False])
@pytest.mark.parametrize("b", [None, 0, 128, 255])
@pytest.mark.parametrize("g", [None, 0, 128, 255])
@pytest.mark.parametrize("r_color", ["#00ff00", (255, 0, 0), 255])
@pytest.mark.parametrize("light", range(5))
def test_set_underlight(GPIO, sn3218, trilobot, light, r_color, g, b, show):
    bot = trilobot.Trilobot()

    # If the first colour is an int, both g and b must be specified
    if isinstance(r_color, int):
        if g is None and b is None:
            with pytest.raises(ValueError):
                bot.set_underlight(light, r_color, g, b, show)
                return
        elif g is None or b is None:
            pytest.skip("Invalid parameters")

    # If the first colour is *not* an int then g and b must be none
    elif isinstance(r_color, (str, tuple)) and (g is not None or b is not None):
        pytest.skip("Invalid parameters")

    else:
        bot.set_underlight(light, r_color, g, b, show)


@pytest.mark.parametrize("light", [99, None, "monkey"])
def test_set_underlight_invalid(GPIO, sn3218, trilobot, light):
    bot = trilobot.Trilobot()
    with pytest.raises((TypeError, ValueError)):
        bot.set_underlight(light, "#ff0000")


@pytest.mark.parametrize("color", [None, 255, (255, 255)])
def test_set_underlight_invalid_color(GPIO, sn3218, trilobot, color):
    bot = trilobot.Trilobot()
    with pytest.raises((TypeError, ValueError)):
        bot.set_underlight(0, color)


@pytest.mark.parametrize("color", [(255, None, 255), (255, 255, None), (-1, -1, -1), (255, -1, -1), (255, 255, -1), (999, 255, 255)])
def test_set_underlight_invalid_color_combo(GPIO, sn3218, trilobot, color):
    bot = trilobot.Trilobot()
    with pytest.raises(ValueError):
        bot.set_underlight(0, *color)


def test_set_underlights(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()

    with pytest.raises(TypeError):
        bot.set_underlights(None, None)

    with pytest.raises(ValueError):
        bot.set_underlights((0, 1, 2, 3, 4, 5, 6, 7, 8), None)

    with pytest.raises(ValueError):
        bot.set_underlights([], None)

    bot.set_underlights((0, 1), "#ff66cc")


def test_set_underlights_hsvg(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()

    bot.set_underlights_hsv((0, 1), 0.5)


def test_set_underlight_hsv(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.set_underlight_hsv(0, 0.5)


def test_fill_underlighting(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.fill_underlighting("#ff66cc")


def test_fill_underlighting_hsv(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.fill_underlighting_hsv(0.5)


def test_clear_underlight(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.clear_underlight(0)


def test_clear_underlighting(GPIO, sn3218, trilobot):
    bot = trilobot.Trilobot()
    bot.clear_underlighting()
