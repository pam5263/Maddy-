@echo off
echo Installing dependencies for MagxxicVOT SMS Tool...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to install dependencies. Please ensure Python and pip are installed and added to your PATH.
    pause
    exit /b %errorlevel%
)
echo.
echo Setup complete successfully!
pause
