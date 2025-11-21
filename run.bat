@echo off
pushd "%~dp0"

:: ============================================
:: Admin Privileges Check
:: ============================================
echo Checking admin privileges...
net session >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] This script requires Administrator privileges!
    echo.
    echo Please right-click run.bat and select "Run as administrator"
    echo.
    goto end
)
color 0A
echo [OK] Running with Administrator privileges
echo.

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
:: UV Check and Installation
:: ============================================
color 0E
echo Checking for uv...

:: Check if uv is installed
where uv >nul 2>nul
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('uv --version 2^>^&1') do set UV_VERSION=%%i
    color 0A
    echo [OK] Found %UV_VERSION%
    echo.
    goto run_script
)

color 0E
echo uv not found. Installing uv...
echo.

:: Try pip first
pip --version >nul 2>nul
if %errorlevel% equ 0 (
    echo Installing uv with pip...
    pip install uv
    if %errorlevel% equ 0 (
        color 0A
        echo [OK] uv installed successfully!
        echo.
        goto run_script
    ) else (
        color 0C
        echo [ERROR] Failed to install uv with pip.
        echo This could be due to network issues or permissions.
        echo.
        goto install_failed
    )
)

:: Try pip3 if pip failed
pip3 --version >nul 2>nul
if %errorlevel% equ 0 (
    echo Installing uv with pip3...
    pip3 install uv
    if %errorlevel% equ 0 (
        color 0A
        echo [OK] uv installed successfully!
        echo.
        goto run_script
    ) else (
        color 0C
        echo [ERROR] Failed to install uv with pip3.
        echo This could be due to network issues or permissions.
        echo.
        goto install_failed
    )
)

:install_failed
color 0C
echo.
echo [ERROR] Could not install uv.
echo.
echo Possible reasons:
echo   - pip/pip3 is not available
echo   - Network connection issues
echo   - Insufficient permissions
echo.
echo Please try manually installing uv:
echo   pip install uv
echo.
goto end

:: ============================================
:: Run the Script
:: ============================================
:run_script
color 0B
echo ============================================
echo Running Genshin Dialogue Auto-Skip...
echo ============================================
echo.
color 0F

uv run autoskip_dialogue.py
set SCRIPT_EXIT_CODE=%errorlevel%

echo.
if %SCRIPT_EXIT_CODE% equ 0 (
    color 0A
    echo ============================================
    echo [SUCCESS] Script completed successfully!
    echo ============================================
    echo.
    goto end
) else (
    color 0C
    echo ============================================
    echo [ERROR] Script exited with error code: %SCRIPT_EXIT_CODE%
    echo ============================================
    echo.
    goto retry_prompt
)

:: ============================================
:: Retry Mechanism
:: ============================================
:retry_prompt
color 0E
set /p RETRY="Would you like to retry? (Y/N): "
if /i "%RETRY%"=="Y" goto run_script
if /i "%RETRY%"=="YES" goto run_script
echo.
echo Exiting...
goto end

:end
color 0F
@pause
