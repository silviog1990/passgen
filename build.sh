#!/bin/bash

if command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    PYTHON_CMD=python3
fi

# Run tests and abort if they fail
$PYTHON_CMD -m unittest discover -s tests
if [ $? -ne 0 ]; then
    echo "❌ Tests failed. Build aborted."
    exit 1
fi

pyinstaller \
    --onefile \
    --windowed \
    --icon=./strong_random_password_generator.icns \
    --name="Strong Random Password Generator" \
    --paths=./strong_random_password_generator \
    strong_random_password_generator/main.py