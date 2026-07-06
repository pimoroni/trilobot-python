import pytest


def test_initialise_servo():
    pytest.skip("Servos wrap pigpio via /var/run/pigpio.pid")
