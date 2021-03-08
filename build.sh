#!/usr/bin/env bash

make clean
./tools/build_nml.py single
make all
