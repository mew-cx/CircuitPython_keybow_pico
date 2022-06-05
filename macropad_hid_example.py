import board
import keypad
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Key order is left to right, top to bottom.
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

# Colors for pressend and not-pressed buttons
ON_COLOR = (0, 0, 255)
OFF_COLOR = (0, 20, 0)

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.4)
neopixels.fill(OFF_COLOR)
kbd = Keyboard(usb_hid.devices)

while True:
    # Get the next keypad event, which might be None.
    event = keys.events.get()
    if event:
        key_number = event.key_number
        # A key transition occurred.
        if event.pressed:
            # Send the keycode for the key that was pressed.
            kbd.press(KEYCODES[key_number])
            # Change its color to give the user feedback.
            neopixels[key_number] = ON_COLOR

        if event.released:
            # Indicate that the key has been released.
            kbd.release(KEYCODES[key_number])
            # Restore the unpressed color.
            neopixels[key_number] = OFF_COLOR