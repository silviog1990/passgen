#!/bin/bash

if command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    PYTHON_CMD=python3
fi

$PYTHON_CMD strong_random_password_generator/main.py