#!/usr/bin/bash
set -xe
python kitten.py src/main.php
scons -j$(nproc --all)
