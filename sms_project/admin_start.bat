@echo off
echo Starting MagxxicVOT Admin Tool...
python admin_keygen.py
if %errorlevel% neq 0 (
    echo.
    echo Tool exited with an error.
    pause
)
