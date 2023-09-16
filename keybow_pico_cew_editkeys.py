# SPDX-FileCopyrightText: 2022-2023 Michael E. Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# mew-cx/CircuitPython_keybow_pico/keybow_pico_cew_editkeys.py -- http://mew.cx 2023-09-16
#
# The "keybow_pico" is a Pimoroni 12-key Keybow which replaces the original
# RaspberryPi Zero with a RaspberryPi Pico using a Red Robotics Pico2Pi
# adapter board.
#
# A configuration of the 12-key "Keybow Pico" with CEW's editing shortcuts.
# (For my lovely Cerrise, to help her doctoral research)

import board
import keypad
import atexit
import usb_hid
from adafruit_dotstar import DotStar
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

__version__ = "0.2.5.5"
__repo__ = "https://github.com/mew-cx/CircuitPython_keybow_pico.git"
__board_id__ = "raspberry_pi_pico"    # board.board_id
__impl_name__ = "circuitpython"       # sys.implementation.name
__impl_version__ = (8, 2, 6)          # sys.implementation.version

# Output devices to receive events from this program.
keybd = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
leds  = DotStar(clock=board.GP2, data=board.GP3, n=12, brightness=0.7)

# keybow_pico key/LED layout (0-11):
#  +-----------+
#  |     KEYBOW|
#  | 0   4   8 |
#  |           |
#  | 1   5   9 |
#  |           |
#  | 2   6  10 |
#  |           |
#  | 3   7  11 |
#  +-----------+
#    USB

MODIFIER = Keycode.CONTROL
KEYDATA = (
    # Table of events to be generated for each key press.
    # Elements of this table must be in Keybow's key/LED order.
    # 0:GPIO pin   1:color    2:pressfunc   3:relfunc       4:eventdata              key/LED#
    ( board.GP16,  0x770077,  keybd.press,  keybd.release,  [MODIFIER, Keycode.Z] ),  #  0
    ( board.GP11,  0x0000ff,  keybd.press,  keybd.release,  [MODIFIER, Keycode.C] ),  #  1  kittykey!
    ( board.GP9,   0x000077,  keybd.press,  keybd.release,  [MODIFIER, Keycode.V] ),  #  2
    ( board.GP7,   0x000077,  keybd.press,  keybd.release,  [MODIFIER, Keycode.A] ),  #  3
    ( board.GP17,  0x777700,  keybd.press,  keybd.release,  [Keycode.BACKSPACE] ),    #  4
    ( board.GP18,  0x777777,  mouse.press,  mouse.release,  [Mouse.RIGHT_BUTTON] ),   #  5
    ( board.GP26,  0x770000,  keybd.press,  keybd.release,  [Keycode.UP_ARROW] ),     #  6
    ( board.GP8,   0x777777,  mouse.press,  mouse.release,  [Mouse.LEFT_BUTTON] ),    #  7
    ( board.GP14,  0x007700,  keybd.press,  keybd.release,  [Keycode.ENTER] ),        #  8
    ( board.GP12,  0x770000,  keybd.press,  keybd.release,  [Keycode.RIGHT_ARROW] ),  #  9
    ( board.GP10,  0x770000,  keybd.press,  keybd.release,  [Keycode.DOWN_ARROW] ),   # 10
    ( board.GP27,  0x770000,  keybd.press,  keybd.release,  [Keycode.LEFT_ARROW] )    # 11
)

@atexit.register
def shutdown():
    """
    At program termination, shutdown cleanly:
    LEDs off, keys/buttons released.
    """
    leds.fill(0)
    keybd.release_all()
    mouse.release_all()

# The main program ##########################################################

def main():
    """Convert keypad events to USB keyboard/mouse events."""
    # Configure GPIO pins for the keys; scan at 20mS (50Hz) for debouncing.
    keys = keypad.Keys([kdata[0] for kdata in KEYDATA],
        interval=0.020, value_when_pressed=False, pull=True)

    # Initialize all keys' LED colors
    leds.fill(0)
    for i,kdata in enumerate(KEYDATA):
        leds[i] = kdata[1]

    # Process key events forever
    while True:
        event = keys.events.get()
        if event is not None:
            _, _, pressfunc, relfunc, eventdata = KEYDATA[event.key_number]
            if event.pressed:
                pressfunc(*eventdata)
            else:
                relfunc(*eventdata)

# vim: set sw=4 ts=8 et ic ai:
