# mew-cx/CircuitPython_keybow_pico/boot.py -- http://mew.cx 2023-09-15
# A keyboard/mouse does not need midi, storage, nor REPL.
# When plugging in, hold the kittykey to go into development mode.

import digitalio
import board
import storage
import usb_cdc
import usb_midi
import usb_hid
from adafruit_dotstar import DotStar

# The kittykey is on pin GP11 and False when pressed.
kittykey = digitalio.DigitalInOut(board.GP11)
kittykey.pull = digitalio.Pull.UP

if kittykey.value == False:
    # kittykey is pressed: leave all default USB enabled.
    print("kittykey sez be in development mode.")
    # all LEDs red, and wait for kittykey release.
    leds = DotStar(clock=board.GP2, data=board.GP3, n=12, brightness=1.0)
    leds.fill(0xff0000)
    while kittykey.value == False:
        pass
    leds.fill(0)
else:
    # kittykey is NOT pressed: disable unneeded USB devices.
    print("kittykey sez just be a keyboard/mouse.")
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_midi.disable()
    usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.MOUSE))

# vim: set sw=4 ts=8 et ic ai:
