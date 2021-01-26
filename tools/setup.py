#!/usr/bin/env python3
# encoding: utf-8

import sys

from setuptools import setup, find_packages


if sys.version_info <= (3, 7):
    raise SystemExit("Python 3.7 or later is required.")

setup(
    name="build_nml",
    version="0.1",
    license="BSD",
    install_requires=[
        'airspeed',
    ],
)
