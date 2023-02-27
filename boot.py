# boot.py
# Turn off unneeded USB devices
import storage
storage.disable_usb_drive()
import usb_midi
usb_midi.disable()
