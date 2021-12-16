# Trilobot

A mid-level robot learning platform aimed at the Rasberry Pi SBC range. Learn more - https://shop.pimoroni.com/products/trilobot

[![Build Status](https://travis-ci.com/pimoroni/trilobot-python.svg?branch=main)](https://travis-ci.com/pimoroni/trilobot-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/trilobot-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/trilobot-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/trilobot.svg)](https://pypi.python.org/pypi/trilobot)
[![Python Versions](https://img.shields.io/pypi/pyversions/trilobot.svg)](https://pypi.python.org/pypi/trilobot)

# Pre-requisites

You must enable:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

# Installing

Stable library from PyPi:

* Just run `pip3 install trilobot`

In some cases you may need to use `sudo` or install pip with: `sudo apt install python3-pip`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/trilobot-python`
* `cd trilobot-python`
* `sudo ./install.sh --unstable`


# Changelog
0.0.1
-----

* Initial Release
