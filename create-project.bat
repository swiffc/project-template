@echo off
rem ================================================================
rem Cursor Development System - Strategic Project Creation Automation
rem ================================================================
rem This batch file orchestrates all the modular components to create
rem a complete development environment following industry best practices
rem
rem Author: Unified Cursor Development System
rem Version: 1.0.0
rem Date: %date%
rem
rem USAGE:
rem   create-project.bat [project-type] [project-name] [options]
rem
rem EXAMPLES:
rem   create-project.bat react-spa my-awesome-app
rem   create-project.bat fastapi-backend my-api --github
rem   create-project.bat windows-automation file-manager --advanced
rem ================================================================

setlocal enabledelayedexpansion

rem ================================================================
rem CONFIGURATION AND CONSTANTS
rem ================================================================
set "SCRIPT_VERSION=1.0.0"
set "SCRIPT_NAME=Cursor Development System"
set "BASE_DIR=%~dp0"
set "MODULES_DIR=%BASE_DIR%modules"
set "TEMPLATES_DIR=%BASE_DIR%templates"
set "OUTPUT_DIR=%BASE_DIR%projects"
set "LOGS_DIR=%BASE_DIR%logs"
set "CONFIG_FILE=%BASE_DIR%config\system.json"

rem Color codes for better UI
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "MAGENTA=[95m"
set "CYAN=[96m"
set "WHITE=[97m"
set "RESET=[0m"

rem Create necessary directories
if not exist "%MODULES_DIR%" mkdir "%MODULES_DIR%"
if not exist "%TEMPLATES_DIR%" mkdir "%TEMPLATES_DIR%"
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"
if not exist "%LOGS_DIR%" mkdir "%LOGS_DIR%"
if not exist "%BASE_DIR%config" mkdir "%BASE_DIR%config"

rem ================================================================
rem LOGGING SYSTEM
rem ================================================================
set "LOG_FILE=%LOGS_DIR%\project-creation-%date:~-4,4%%date:~-10,2%%date:~-7,2%.log"

:log
echo [%time%] %~1 >> "%LOG_FILE%"
echo %GREEN%[%time%] %~1%RESET%
goto :eof

:error_log
echo [%time%] ERROR: %~1 >> "%LOG_FILE%"
echo %RED%[ERROR] %~1%RESET%
goto :eof

:warning_log
echo [%time%] WARNING: %~1 >> "%LOG_FILE%"
echo %YELLOW%[WARNING] %~1%RESET%
goto :eof

rem ================================================================
rem BANNER AND INITIALIZATION
rem ================================================================
:show_banner
cls
echo %CYAN%
echo ================================================================
echo    %SCRIPT_NAME% v%SCRIPT_VERSION%
echo ================================================================
echo    Strategic Project Creation Automation
echo    Integrating: File Organization ^| Validation ^| Consistency
echo                Templates ^| Auto-Development ^| GitHub Integration
echo ================================================================
echo %RESET%
goto :eof

rem ================================================================
rem HELP SYSTEM
rem ================================================================
:show_help
call :show_banner
echo %WHITE%
echo USAGE:
echo   %~nx0 [project-type] [project-name] [options]
echo.
echo PROJECT TYPES:
echo   react-spa          - Modern React Single Page Application
echo   nextjs-fullstack   - Next.js Full-Stack Application
echo   vue-nuxt          - Vue.js with Nuxt Framework
echo   express-api       - Express.js REST API
echo   fastapi-backend   - FastAPI Python Backend
echo   electron-desktop  - Electron Desktop Application
echo   react-native      - React Native Mobile App
echo   flutter-mobile    - Flutter Mobile Application
echo   python-automation - Python Automation Scripts
echo   windows-automation- PowerShell Windows Automation
echo   cad-automation    - CAD Automation (AutoCAD/SolidWorks)
echo   ai-ml-project     - AI/ML Project with TensorFlow/PyTorch
echo   static-website    - Static Website with Modern Tooling
echo.
echo OPTIONS:
echo   --github          - Initialize GitHub repository
echo   --advanced        - Include advanced features and configurations
echo   --template=NAME   - Use specific template variant
echo   --output=PATH     - Specify output directory
echo   --no-install      - Skip dependency installation
echo   --help            - Show this help message
echo.
echo EXAMPLES:
echo   %~nx0 react-spa my-awesome-app --github
echo   %~nx0 fastapi-backend my-api --advanced --output=C:\Projects
echo   %~nx0 windows-automation file-manager
echo %RESET%
goto :eof

rem ... (script continues as provided) ...
