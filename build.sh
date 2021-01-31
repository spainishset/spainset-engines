#!/usr/bin/env bash

make clean
./tools/build_nml.py steam
./tools/build_nml.py diesel
./tools/build_nml.py electric
./tools/build_nml.py emu
./tools/build_nml.py mmu
make all
