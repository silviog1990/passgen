#!/bin/bash

if command -v python &>/dev/null; then
    python strong_random_password_generator/main.py
else
    python3 strong_random_password_generator/main.py
fi