#!/bin/bash

# Esegui i test e interrompi se falliscono
python3 -m unittest discover -s tests
if [ $? -ne 0 ]; then
    echo "❌ Test falliti. Build interrotta."
    exit 1
fi

pyinstaller \
    --onefile \
    --windowed \
    --icon=/Users/s1lv10/workspace/python/strong_random_password_generator/strong_random_password_generator.icns \
    --name="Strong Random Password Generator" \
    --paths=./strong_random_password_generator \
    strong_random_password_generator/main.py