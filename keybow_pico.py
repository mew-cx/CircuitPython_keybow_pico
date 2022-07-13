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

KEYDATA = (
    ( board.GP16, Keycode.ZERO ),
    ( board.GP11, Keycode.THREE ),
    ( board.GP9,  Keycode.SIX ),
    ( board.GP7,  Keycode.NINE ),
    ( board.GP17, Keycode.ONE ),
    ( board.GP18, Keycode.FOUR ),
    ( board.GP26, Keycode.SEVEN ),
    ( board.GP8,  Keycode.BACKSPACE ),
    ( board.GP14, Keycode.TWO ),
    ( board.GP12, Keycode.FIVE ),
    ( board.GP10, Keycode.EIGHT ),
    ( board.GP27, Keycode.ENTER ),
)

keys = keypad.Keys([i[0] for i in KEYDATA], value_when_pressed=False, pull=True)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

ON_COLOR = 0x0000ff
OFF_COLOR = 0x001800
dots = adafruit_dotstar.DotStar(board.GP2, board.GP3, 12, brightness=0.1)
dots.fill(0xff0000)

@atexit.register
def clear():
    dots.fill(0)

def HandleKey(key, is_pressed):
    if is_pressed:
        dots[key] = ON_COLOR
        kbd.press(KEYDATA[key][1])
        #layout.write(KEYSTRING[key])
    else:
        dots[key] = OFF_COLOR
        kbd.release(KEYDATA[key][1])

while True:
    event = keys.events.get()
    if event:
        print(repr(event))
        HandleKey(event.key_number, event.pressed)
    else:
        pass

# vim: set sw=4 ts=8 et ic ai:
