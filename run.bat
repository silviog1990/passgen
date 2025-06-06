@echo off
where python >nul 2>nul
if %ERRORLEVEL%==0 (
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=python3
)
%PYTHON_CMD% strong_random_password_generator\main.py
