# README.txt
## Setup (DRAFT)
```bash
# using gitbash
cd /e
git clone --separate-git-dir=/c/mew/gits/dust_runtime_KEYBOW.git git@github.com:mew-cx/dust_runtime.git
mv dust_runtime/.git .
rmdir dust_runtime/
git checkout -f keybow_pico
```

## References
- https://shop.pimoroni.com/products/keybow
- https://pinout.xyz/pinout/keybow

- Revamping a Pi Keybow into a Pico Keybow.url
- https://codepope.dev/post/revamping-pi-keybow-into-pico-keybow/
- codepope-KeyBow-Pico-CircuitPython- CircuitPython code for driving a Keybow keyboard from Pimoroni using a Pi Pico (on a Pico.url
- https://github.com/codepope/KeyBow-Pico-CircuitPython

- The Keybow - Ben Madley's Blog.url
- https://benmadley.co.uk/2019/08/30/keybow.html

- https://redrobotics.co.uk/
- https://www.tindie.com/stores/redrobotics/
- https://www.tindie.com/products/redrobotics/pico-2-pi-adapter-board/
- https://github.com/RedRobotics

- https://github.com/DougieWougie/MouseJiggler

## Ideas
Add: mousejiggler ability
Add: some communications API from host system to set
- LED colors.
- keybindings.
- enable/disable mousejiggler

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

#eof
