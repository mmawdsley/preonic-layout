#!/usr/bin/env bash

set -o nounset
set -o errexit

qmk flash -kb preonic/rev3 -km mmawdsley
