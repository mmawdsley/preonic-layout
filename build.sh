#!/usr/bin/env bash

set -o nounset
set -o errexit

if test -f "keymap.json"; then
    rm keymap.json
fi

qmk compile -kb preonic/rev3 -km mmawdsley
qmk c2json -kb preonic/rev3 -km mmawdsley --no-cpp -o keymap.json keymap.c
python3 layout_generator.py
rm keymap.json
