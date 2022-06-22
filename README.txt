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
