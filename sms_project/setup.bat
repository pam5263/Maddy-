@echo off
echo Installing dependencies for MagxxicVOT SMS Tool...
python -m pip install --upgrade pip
python -m pip install setuptools
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
