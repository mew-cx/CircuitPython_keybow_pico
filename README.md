## Clone
```bash
# using gitbash
# Go to the CircuitPython device.
cd /e
# Clone the repo, but put the .git/ database somewhere _other_ than the CPy device.
git clone  --separate-git-dir=/c/mew/gits/github.com/mew-cx/CircuitPython_keybow_pico.git  git@github.com:mew-cx/CircuitPython_keybow_pico.git  mew_keybow_pico
```

## Physical Key/LED numbering
```
+--------------------------+
|             K E Y B O W  |
+--------+--------+--------+
|        |        |        |
|    0   |    4   |    8   |
|        |        |        |
+--------+--------+--------+
|        |        |        |
|    1   |    5   |    9   |
|        |        |        |
+--------+--------+--------+
|        |        |        |
|    2   |    6   |   10   |
|        |        |        |
+--------+--------+--------+
|        |        |        |
|    3   |    7   |   11   |
|        |        |        |
+--------+--------+--------+
      USB

 +-----------+
 |     KEYBOW|
 | 0   4   8 |
 |           |
 | 1   5   9 |
 |           |
 | 2   6  10 |
 |           |
 | 3   7  11 |
 +-----------+
   USB
```

## References
- Pimoroni Keybow
<br>https://shop.pimoroni.com/products/keybow
<br>https://pinout.xyz/pinout/keybow

- Red Robotics
<br>https://redrobotics.co.uk/
<br>https://www.tindie.com/stores/redrobotics/
<br>https://www.tindie.com/products/redrobotics/pico-2-pi-adapter-board/
<br>https://github.com/RedRobotics

- Revamping a Pi Keybow into a Pico Keybow
<br>https://codepope.dev/post/revamping-pi-keybow-into-pico-keybow/
<br>https://github.com/codepope/KeyBow-Pico-CircuitPython

- The Keybow - Ben Madley's Blog
<br>https://benmadley.co.uk/2019/08/30/keybow.html

- https://github.com/DougieWougie/MouseJiggler

## Ideas
- Add: mousejiggler ability
- Add: some communications API from host system to set
<br>LED colors.
<br>keybindings.
<br>enable/disable mousejiggler

#eof
