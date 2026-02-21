@echo off
echo Starting MagxxicVOT SMS Tool...
python sms_tool.py
if %errorlevel% neq 0 (
    echo.
    echo Tool exited with an error.
    echo.
    echo If you see "ModuleNotFoundError: No module named 'pkg_resources'",
    echo please run setup.bat again to install necessary components.
    pause
)
