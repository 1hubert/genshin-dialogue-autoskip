@echo off
pushd "%~dp0"


:: ============================================
:: Python Installation Check
:: ============================================
color 0E
echo Checking for Python...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    goto end
)

:: Display Python version
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
color 0A
echo [OK] Found %PYTHON_VERSION%
echo.


:: ============================================
:: Creating venv and installing dependencies
:: ============================================

python -m venv venv
venv\Scripts\python.exe -m pip install --no-cache-dir -r requirements.txt




:: ============================================
:: Install ViGEmBus
:: ============================================

setlocal EnableExtensions

set "URL=https://github.com/nefarius/ViGEmBus/releases/download/v1.22.0/ViGEmBus_1.22.0_x64_x86_arm64.exe"
set "FILE=ViGEmBus_1.22.0_x64_x86_arm64.exe"
set "TARGET_VER=1.22.0"


echo.
echo Downloading ViGEmBus installer to: "%CD%\%FILE%"
curl -L -o "%FILE%" "%URL%"


echo.
echo Launching installer (interactive)...
"%CD%\%FILE%"

echo.
echo Installer launched. If it was already installed, it should offer repair/update as needed.
endlocal

:end
@pause