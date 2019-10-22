#!/bin/bash

INSTALLED=`python3 -V`
if [[ $INSTALLED != *"Python 3"* ]]; then
    echo "Please Install Python3"
    exit 1
fi
pip=`pip --version`
if [[ $pip == *"command"* ]];then
    echo "Please Install Pip"
    exit 1
fi
NUMPY=`python -c "import numpy"`
PYOPENGL=`python -c "from OpenGL.GL import *"`
PYGAME=`python -c "import pygame"`
if [[ ! -z "$NUMPY" ]]; then
    pip install numpy
fi
if [[ ! -z "$PYOPENGL" ]]; then
    pip install pyopengl
fi
if [[ ! -z "$PYGAME" ]]; then
    pip install pygame
fi
MAP=$1
if [[ -z "$MAP" ]]; then
MAP="resources/mod1_files/5x5.mod1"
fi
python src/main.py $MAP
