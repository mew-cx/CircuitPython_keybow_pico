# SPDX-FileCopyrightText: 2022 Michael E. Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# keybow_pico.py -- http://mew.cx/ 2022-07-07


import board
import keypad
import adafruit_dotstar
import atexit

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

#from adafruit_hid.consumer_control import ConsumerControl
#from adafruit_hid.consumer_control_code import ConsumerControlCode


@atexit.register
def clear():
    dots.fill(OFF_COLOR)

KEY_PINS = (
    board.GP16,
    board.GP11,
    board.GP9,
    board.GP7,
    board.GP17,
    board.GP18,
    board.GP26,
    board.GP8,
    board.GP14,
    board.GP12,
    board.GP10,
    board.GP27,
)

KEYCODES = (
    Keycode.NINE,
    Keycode.SIX,
    Keycode.THREE,
    Keycode.ZERO,
    Keycode.BACKSPACE,
    Keycode.SEVEN,
    Keycode.FOUR,
    Keycode.ONE,
    Keycode.ENTER,
    Keycode.EIGHT,
    Keycode.FIVE,
    Keycode.TWO,
)


keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

ON_COLOR = 0x0000ff
OFF_COLOR = 0x001800
dots = adafruit_dotstar.DotStar(board.GP2, board.GP3, 12, brightness=0.1)
clear()
#dots.fill(OFF_COLOR)

while True:
    event = keys.events.get()
    if event:
        print(event)
        i = event.key_number
        if event.pressed:
            dots[i] = ON_COLOR
            kbd.press(KEYCODES[i])
            #layout.write(KEYSTRING[i])
        else:
            dots[i] = OFF_COLOR
            kbd.release(KEYCODES[i])

# vim: set sw=4 ts=8 et ic ai:
