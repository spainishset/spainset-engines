#!/usr/bin/env bash

make clean
./tools/build_nml.py steam
./tools/build_nml.py single
./tools/build_nml.py mu
./tools/build_nml.py wagons
make all
