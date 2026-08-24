import sys
from unittest import mock

import pytest


@pytest.fixture(scope="session")
def GPIO():
    """Mock RPi.GPIO module."""
    GPIO = mock.MagicMock()
    sys.modules["RPi"] = mock.Mock()
    sys.modules["RPi"].GPIO = GPIO
    sys.modules["RPi.GPIO"] = GPIO
    yield GPIO
    del sys.modules["RPi"]


@pytest.fixture(scope="session")
def sn3218():
    """Mock sn3218 module."""
    sys.modules["sn3218"] = mock.MagicMock()
    yield sys.modules["sn3218"]
    del sys.modules["sn3218"]


@pytest.fixture(scope="session")
def trilobot():
    import trilobot
    yield trilobot
    del sys.modules["trilobot"]
