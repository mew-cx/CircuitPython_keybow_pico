# keybow_pico

::::::::::::::
setup.txt
::::::::::::::

```bash
# using gitbash
cd /e
git clone --separate-git-dir=/c/mew/gits/dust_runtime_KEYBOW.git git@github.com:mew-cx/dust_runtime.git
mv dust_runtime/.git .
rmdir dust_runtime/
git checkout -f keybow_pico
```

::::::::::::::
.git
::::::::::::::
gitdir: C:/mew/tmp/dust_runtime_KEYBOW.git

::::::::::::::
references
::::::::::::::
https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html


::::::::::::::
codepope-KeyBow-Pico-CircuitPython- CircuitPython code for driving a Keybow keyboard from Pimoroni using a Pi Pico (on a Pico.url
https://github.com/codepope/KeyBow-Pico-CircuitPython
::::::::::::::
Revamping a Pi Keybow into a Pico Keybow.url
https://codepope.dev/post/revamping-pi-keybow-into-pico-keybow/
::::::::::::::
The Keybow - Ben Madley's Blog.url
https://benmadley.co.uk/2019/08/30/keybow.html
::::::::::::::

=============================================================================

https://codepope.dev/post/revamping-pi-keybow-into-pico-keybow/

https://docs.circuitpython.org/projects/hid/en/latest/
https://docs.circuitpython.org/projects/board-toolkit/en/latest/
https://docs.circuitpython.org/en/latest/shared-bindings/keypad/
https://docs.circuitpython.org/en/latest/shared-bindings/usb_cdc/

https://shop.pimoroni.com/products/keybow
https://pinout.xyz/pinout/keybow
https://www.tindie.com/products/redrobotics/pico-2-pi-adapter-board/

https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-hid-keyboard
https://learn.adafruit.com/customizing-usb-devices-in-circuitpython
https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage

https://github.com/codepope/KeyBow-Pico-CircuitPython
https://github.com/adafruit/Adafruit_CircuitPython_HID
https://github.com/DougieWougie/MouseJiggler


TODO
a communications channel from host to keybow, to permit host control of:
* LEDs.
* keybindings

=============================================================================
https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#usb-serial-console-repl-and-data-3096590
https://docs.circuitpython.org/en/latest/shared-bindings/usb_cdc/

# MUST BE IN boot.py!!
import usb_cdc

# Disable both serial devices.
usb_cdc.disable()

# Enable just console (the default setting)
usb_cdc.enable(console=True, data=False)
  
# Enable console and data
usb_cdc.enable(console=True, data=True)

# Disable both. Same as usb_cdc.disable()
usb_cdc.enable(console=False, data=False)

https://github.com/adafruit/Adafruit_Board_Toolkit
You can list the available usb_cdc.data serial ports using adafruit_board_toolkit.circuitpython_serial.data_comports().
Similarly, to get a list of the usb_cdc.console (REPL) serial ports, use adafruit_board_toolkit.circuitpython.repl_comports().

=============================================================================


=============================================================================
#eof
