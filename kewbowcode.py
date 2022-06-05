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
