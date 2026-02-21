@echo off
echo Starting MagxxicVOT SMS Tool...
python sms_tool.py
if %errorlevel% neq 0 (
    echo.
    echo Tool exited with an error.
    pause
)
