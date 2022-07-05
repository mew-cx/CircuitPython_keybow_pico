::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
macropad_hid_example.py
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import board
import keypad
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

KEY_PINS = (
    board.KEY1,
    board.KEY2,
    board.KEY3,
    board.KEY4,
    board.KEY5,
    board.KEY6,
    board.KEY7,
    board.KEY8,
    board.KEY9,
    board.KEY10,
    board.KEY11,
    board.KEY12,
)

# Keycodes to send corresponding to the keys above.
KEYCODES = (
    Keycode.SEVEN,
    Keycode.EIGHT,
    Keycode.NINE,
    Keycode.FOUR,
    Keycode.FIVE,
    Keycode.SIX,
    Keycode.ONE,
    Keycode.TWO,
    Keycode.THREE,
    Keycode.BACKSPACE,
    Keycode.ZERO,
    Keycode.ENTER,
)

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.4)
kbd = Keyboard(usb_hid.devices)

ON_COLOR = (0, 0, 255)
OFF_COLOR = (0, 20, 0)
neopixels.fill(OFF_COLOR)

while True:
    event = keys.events.get()
    if event:
        print(event)
        key_number = event.key_number

        if event.pressed:
            neopixels[key_number] = ON_COLOR
            kbd.press(KEYCODES[key_number])

        if event.released:
            neopixels[key_number] = OFF_COLOR
            kbd.release(KEYCODES[key_number])

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
keybow_dotstar.py
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
kewbowcode.py
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# kewbowcode.py

import board
import digitalio
import adafruit_dotstar

import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

pixels = adafruit_dotstar.DotStar(board.GP2, board.GP3, 12)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

class KeyLight:
    def __init__(self,keynum,pinnum,lednum,press_string,press_func):
        self.keynum = keynum
        self.pinnum = pinnum
        self.lednum = lednum
        self.press_string = press_string
        self.press_func = press_func
        self.pressed = False
        self.pin = digitalio.DigitalInOut(self.pinnum)
        self.pin.switch_to_input(pull = digitalio.Pull.UP)
        self.base_color = (self.keynum*20, 0, 255-(self.keynum*20), 0.5)
        self.set_pixel(self.base_color)

    def set_pixel(self,color):
        pixels[self.lednum] = color

    def get_pixel(self):
        return pixels[self.lednum]

    def key_down(self):
        return self.pin.value == False

macro_n = 0

def key_macroinckey(kdb,layout):
    global macro_n
    layout.write(f"Macro {macro_n}")
    macro_n += 1

# def key_undo(kdb,layout):
#     kbd.press(Keycode.COMMAND,Keycode.Z)
#     kbd.release_all()

keyArray = []
keyArray.append( KeyLight( 0, board.GP7,   3,  None, key_macroinckey))
keyArray.append( KeyLight( 1, board.GP8,   7,  "1",  None))
keyArray.append( KeyLight( 2, board.GP27,  11, "2",  None))
keyArray.append( KeyLight( 3, board.GP9,   2,  "3",  None))
keyArray.append( KeyLight( 4, board.GP26,  6,  "4",  None))
keyArray.append( KeyLight( 5, board.GP10,  10, "5",  None))
keyArray.append( KeyLight( 6, board.GP11,  1,  "6",  None))
keyArray.append( KeyLight( 7, board.GP18,  5,  "7",  None))
keyArray.append( KeyLight( 8, board.GP12,  9,  "8",  None))
keyArray.append( KeyLight( 9, board.GP16,  0,  "9",  None))
keyArray.append( KeyLight( 10, board.GP17, 4,  "Ten", None))
keyArray.append( KeyLight( 11, board.GP14, 8,  "Eleven", None))

while True:
    for k in keyArray:
        if k.key_down():
            if not k.pressed:
                k.pressed = True
                k.set_pixel((255,255,255,0.5))
                if k.press_func:
                    k.press_func(kbd,layout)
                else:
                    layout.write(k.press_string)
            else:
                pass    # held down behaviour here
        elif k.pressed:
                k.pressed = False
                k.set_pixel(k.base_color)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
adafruit_macropad_demo.py
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Keypad and rotary encoder example for Adafruit MacroPad"""
import board
import digitalio
import rotaryio
import neopixel
import keypad
from rainbowio import colorwheel


key_pins = (board.KEY1, board.KEY2, board.KEY3, board.KEY4, board.KEY5, board.KEY6,
            board.KEY7, board.KEY8, board.KEY9, board.KEY10, board.KEY11, board.KEY12)
keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)

encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.2)

last_position = None
while True:
    if not button.value:
        pixels.brightness = 1.0
    else:
        pixels.brightness = 0.2

    position = encoder.position
    if last_position is None or position != last_position:
        print("Rotary:", position)
    last_position = position

    color_value = (position * 2) % 255

    event = keys.events.get()
    if event:
        print(event)
        if event.pressed:
            pixels[event.key_number] = colorwheel(color_value)
        else:
            pixels[event.key_number] = 0
