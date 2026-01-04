@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------
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
:: Starting script
:: ============================================

venv\Scripts\python.exe autoskip_dialogue.py


:end
@pause