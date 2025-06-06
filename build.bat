@echo off
where python >nul 2>nul
if %ERRORLEVEL%==0 (
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=python3
)

%PYTHON_CMD% -m unittest discover -s tests
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Tests failed. Build aborted.
    exit /b 1
)

pyinstaller ^
    --onefile ^
    --windowed ^
    --icon=strong_random_password_generator.icns ^
    --name="Strong Random Password Generator" ^
    --paths=strong_random_password_generator ^
    strong_random_password_generator\main.py
