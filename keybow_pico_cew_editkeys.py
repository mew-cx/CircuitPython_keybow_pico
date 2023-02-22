# SPDX-FileCopyrightText: 2022 Michael E. Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# keybow_pico.py -- http://mew.cx/ 2023-02-17

import board
import keypad
import adafruit_dotstar
import atexit
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

__version__ = "0.1.0.1"
__repo__ = "https://github.com/mew-cx/CircuitPython_keybow_pico"

dots = adafruit_dotstar.DotStar(board.GP2, board.GP3, 12, brightness=0.5)
dots.fill(0x800000)

KEYDATA = (
    ( board.GP16, Keycode.ZERO ),
    ( board.GP17, Keycode.ONE ),
    ( board.GP14, Keycode.TWO ),
    ( board.GP11, Keycode.THREE ),
    ( board.GP18, Keycode.FOUR ),
    ( board.GP12, Keycode.FIVE ),
    ( board.GP9,  Keycode.SIX ),
    ( board.GP26, Keycode.SEVEN ),
    ( board.GP10, Keycode.EIGHT ),
    ( board.GP7,  Keycode.NINE ),
    ( board.GP8,  Keycode.BACKSPACE ),
    ( board.GP27, Keycode.ENTER ),
)

keys = keypad.Keys([i[0] for i in KEYDATA], value_when_pressed=False, pull=True)
kbd = Keyboard(usb_hid.devices)

@atexit.register
def clear():
    dots.fill(0)

def HandleKey(knum, is_pressed):
    ON_COLOR  = 0x0000ff
    OFF_COLOR = 0x001800
    MODIFIER = Keycode.CONTROL

    if not is_pressed:
        kbd.release_all()
    elif knum == 0:
        kbd.press(MODIFIER, Keycode.Z)
    elif knum == 2:
        kbd.press(Keycode.ENTER)
    elif knum == 3:
        kbd.press(MODIFIER, Keycode.C)
    elif knum == 6:
        kbd.press(MODIFIER, Keycode.V)
    elif knum == 9:
        kbd.press(MODIFIER, Keycode.A)

while True:
    event = keys.events.get()
    if event:
        HandleKey(event.key_number, event.pressed)

# vim: set sw=4 ts=8 et ic ai:
