::::::::::::::
setup.txt
::::::::::::::
git clone -n --separate-git-dir=/c/mew/tmp/dust_runtime_KEYBOW.git https://github.com/mew-cx/dust_runtime.git
mv dust_runtime/.git .
rmdir dust_runtime/
git checkout -f keybow_pico

git clone --separate-git-dir=C:/mew/gits/dust_runtime_KEYBOW.git git@github.com:mew-cx/dust_runtime.git e:/REPO

::::::::::::::
.git
::::::::::::::
gitdir: C:/mew/tmp/dust_runtime_KEYBOW.git


::::::::::::::
references
::::::::::::::
https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html
