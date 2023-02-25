# SPDX-FileCopyrightText: 2022-2023 Michael E. Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# keybow_pico_cew_editkeys.py -- http://mew.cx/ 2023-02-24
# A configuration of the 12-key "Keybow Pico" for CEW's editing shortcuts.

#import time
import board
import keypad
import adafruit_dotstar
import atexit
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

__version__ = "0.2.0.0"
__repo__ = "https://github.com/mew-cx/CircuitPython_keybow_pico"

# Output devices to receive events from this program.
keybd = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
leds  = adafruit_dotstar.DotStar(board.GP2, board.GP3, 12, brightness=0.5)

# Elements of this table are in Keybow's key/LED order (0-11).
MODIFIER = Keycode.CONTROL
KEYINFO = (
    # GPIO pin     color      pressfunc     relfunc         eventdata                keynumber
    ( board.GP16,  0xff00ff,  keybd.press,  keybd.release,  [MODIFIER, Keycode.Z]),  #  0
    ( board.GP11,  0x0000ff,  keybd.press,  keybd.release,  [MODIFIER, Keycode.C]),  #  1
    ( board.GP9,   0x0000ff,  keybd.press,  keybd.release,  [MODIFIER, Keycode.V]),  #  2
    ( board.GP7,   0x0000ff,  keybd.press,  keybd.release,  [MODIFIER, Keycode.A]),  #  3
    ( board.GP17,  0xffff00,  keybd.press,  keybd.release,  [Keycode.BACKSPACE]),    #  4
    ( board.GP18,  0x777777,  mouse.press,  mouse.release,  [Mouse.RIGHT_BUTTON]),   #  5
    ( board.GP26,  0xff0000,  keybd.press,  keybd.release,  [Keycode.UP_ARROW]),     #  6
    ( board.GP8,   0x777777,  mouse.press,  mouse.release,  [Mouse.LEFT_BUTTON]),    #  7
    ( board.GP14,  0x00ff00,  keybd.press,  keybd.release,  [Keycode.ENTER]),        #  8
    ( board.GP12,  0xff0000,  keybd.press,  keybd.release,  [Keycode.RIGHT_ARROW]),  #  9
    ( board.GP10,  0xff0000,  keybd.press,  keybd.release,  [Keycode.DOWN_ARROW]),   # 10
    ( board.GP27,  0xff0000,  keybd.press,  keybd.release,  [Keycode.LEFT_ARROW])    # 11
)

# At program termination, shutdown cleanly: LEDs off, keys/buttons released.
@atexit.register
def shutdown():
    leds.fill(0)
    keybd.release_all()
    mouse.release_all()

def main():
    # Assign GPIO pins to keypad keys, and scan @ 50Hz (20mS) for debouncing.
    keys = keypad.Keys([i[0] for i in KEYINFO], interval=0.02, value_when_pressed=False, pull=True)

    # Set the keypad's LED colors
    leds.fill(0)
    for knum,kinfo in enumerate(KEYINFO):
        leds[knum] = kinfo[1]

    while True:
        event = keys.events.get()
        if event:
            kinfo     = KEYINFO[event.key_number]
            pressfunc = kinfo[2]
            relfunc   = kinfo[3]
            eventdata = kinfo[4]
            if event.pressed:
                pressfunc(*eventdata)
            else:
                relfunc(*eventdata)

main()

# vim: set sw=4 ts=8 et ic ai:
