# dust_dotstar.py -- http://mew.cx/ 2022-06-04
# SPDX-FileCopyrightText: 2022 Mike Weiblen

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import random
import board
import atexit
import adafruit_dotstar as dotstar

# dotstar strip on hardware SPI
dots = dotstar.DotStar(board.GP2, board.GP3, 12, brightness=0.1)
n_dots = len(dots)

def random_color():
    #return random.randrange(0,8) << 5
    return random.randrange(0,256)

@atexit.register
def clear():
    for dot in range(n_dots):
        dots[dot] = (0,0,0)

while True:
    for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())

    time.sleep(0.25)
