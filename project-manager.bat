@echo off
title Project Manager v1.0
color 0A
:menu
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║              PROJECT MANAGER                 ║
echo ║           Development Toolkit                ║
echo ╚══════════════════════════════════════════════╝
echo.
echo  📊 1. Start Development Server
echo  🚀 2. Quick Commit (Version Number)
echo  ✏️  3. Custom Commit Message
echo  📋 4. View Git Status
echo  🔧 5. Project Info
echo  📦 6. Install Dependencies
echo  🔄 7. Pull Latest Changes
echo  ❌ 8. Exit
echo.
echo ──────────────────────────────────────────────
set /p choice="Choose an option (1-8): "

if "%choice%"=="1" goto start_server
if "%choice%"=="2" goto quick_commit
if "%choice%"=="3" goto custom_commit
if "%choice%"=="4" goto git_status
if "%choice%"=="5" goto project_info
if "%choice%"=="6" goto install_deps
if "%choice%"=="7" goto pull_changes
if "%choice%"=="8" goto exit
echo ❌ Invalid choice. Please select 1-8.
timeout /t 2 >nul
goto menu

:start_server
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║             STARTING DEV SERVER             ║
echo ╚══════════════════════════════════════════════╝
echo.

REM Check prerequisites
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js not found! Please install Node.js first.
    echo    Download from: https://nodejs.org/
    pause
    goto menu
)

where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ NPM not found! Please install Node.js first.
    pause
    goto menu
)

echo ✅ Node.js and NPM found
echo.

REM Check if in correct directory
if not exist "package.json" (
    echo ❌ package.json not found!
    echo    Make sure you're in the project directory
    pause
    goto menu
)

echo ✅ Project files found
echo.

REM Install dependencies if needed
if not exist "node_modules" (
    echo 📦 Installing dependencies...
    npm install
    if %errorlevel% neq 0 (
        echo ❌ Failed to install dependencies
        pause
        goto menu
    )
    echo ✅ Dependencies installed
    echo.
)

REM Detect server start command
set "start_cmd="
if exist "server/index.ts" set "start_cmd=npx tsx server/index.ts"
if exist "server/index.js" set "start_cmd=node server/index.js"
if exist "index.ts" set "start_cmd=npx tsx index.ts"
if exist "index.js" set "start_cmd=node index.js"

REM Check package.json for dev script
if "%start_cmd%"=="" (
    npm run dev 2>nul
    if %errorlevel% equ 0 (
        set "start_cmd=npm run dev"
    ) else (
        echo ❌ No server entry point found!
        echo    Expected: server/index.ts, index.ts, or npm run dev
        pause
        goto menu
    )
)

REM Check if port is available (try common ports)
for %%p in (3000 5000 8000) do (
    netstat -an | find "127.0.0.1:%%p" >nul
    if %errorlevel% neq 0 (
        echo ✅ Port %%p available
        goto start_server_now
    )
)

echo ⚠️  Common ports may be in use
echo.

:start_server_now
echo 🚀 Starting Development Server...
echo 📁 Project: %CD%
echo.
echo ──────────────────────────────────────────────
echo Press Ctrl+C to stop server, then any key to return to menu
echo ──────────────────────────────────────────────
echo.

%start_cmd%
echo.
echo 🛑 Server stopped
pause
goto menu

:quick_commit
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║            QUICK VERSION COMMIT              ║
echo ╚══════════════════════════════════════════════╝
echo.

REM Check if git is available
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git not found! Please install Git first.
    echo    Download from: https://git-scm.com/
    pause
    goto menu
)

REM Check if in git repository
if not exist ".git" (
    echo ❌ Not a Git repository!
    echo    Initialize git with: git init
    pause
    goto menu
)

REM Check for remote origin
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ No remote repository configured!
    echo    Add remote with: git remote add origin <url>
    pause
    goto menu
)

echo ✅ Git repository found
echo 🔗 Remote: 
git remote get-url origin
echo.

REM Show current status
echo 📋 Current changes:
git status --porcelain
echo.
echo ──────────────────────────────────────────────
set /p version="📝 Enter version (e.g., v1.0, v1.1, v2.0): "

if "%version%"=="" (
    echo ❌ No version entered
    timeout /t 2 >nul
    goto menu
)

echo.
echo 📦 Adding all changes...
git add .
if %errorlevel% neq 0 (
    echo ❌ Failed to add changes
    pause
    goto menu
)

echo 💾 Committing as %version%...
git commit -m "%version%"
if %errorlevel% neq 0 (
    echo ❌ Commit failed (no changes or error)
    pause
    goto menu
)

echo 🚀 Pushing to repository...
git push origin main
if %errorlevel% neq 0 (
    git push origin master
    if %errorlevel% neq 0 (
        echo ❌ Push failed - check network/credentials
        pause
        goto menu
    )
)

echo.
echo ✅ Successfully committed and pushed %version%!
echo 🎉 Changes are now live on repository
timeout /t 3 >nul
goto menu

:custom_commit
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║           CUSTOM COMMIT MESSAGE             ║
echo ╚══════════════════════════════════════════════╝
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git not found!
    pause
    goto menu
)

if not exist ".git" (
    echo ❌ Not a Git repository!
    pause
    goto menu
)

echo 📋 Current changes:
git status --short
echo.
echo ──────────────────────────────────────────────

:input_message
set /p message="✏️  Enter commit message: "
if "%message%"=="" (
    echo ❌ Message cannot be empty
    goto input_message
)

echo.
echo 📦 Adding changes...
git add .

echo 💾 Committing: "%message%"
git commit -m "%message%"
if %errorlevel% neq 0 (
    echo ❌ Commit failed
    pause
    goto menu
)

echo 🚀 Pushing to repository...
git push origin main 2>nul || git push origin master
if %errorlevel% neq 0 (
    echo ❌ Push failed - check connection
    pause
    goto menu
)

echo.
echo ✅ Successfully committed and pushed!
timeout /t 3 >nul
goto menu

:git_status
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║              GIT STATUS REPORT               ║
echo ╚══════════════════════════════════════════════╝
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git not installed
    pause
    goto menu
)

if not exist ".git" (
    echo ❌ Not a Git repository
    pause
    goto menu
)

echo 🔗 Repository Information:
git remote get-url origin 2>nul
echo.

echo 🌿 Current Branch:
git branch --show-current
echo.

echo 📋 Working Directory Status:
git status --short
echo.

echo 📜 Recent Commits (Last 5):
git log --oneline -5 --decorate
echo.

pause
goto menu

:project_info
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║             PROJECT INFORMATION              ║
echo ╚══════════════════════════════════════════════╝
echo.

echo 💻 System Information:
echo ──────────────────────────────────────────────
echo 📁 Current Directory: %CD%
echo 👤 User: %USERNAME%
echo ⏰ Date/Time: %DATE% %TIME%
echo.

echo 🔧 Environment Check:
where node >nul 2>&1 && (echo ✅ Node.js: & node --version) || echo ❌ Node.js: Not installed
where npm >nul 2>&1 && (echo ✅ NPM: & npm --version) || echo ❌ NPM: Not installed
where git >nul 2>&1 && (echo ✅ Git: & git --version) || echo ❌ Git: Not installed
echo.

echo 📦 Project Files:
if exist "package.json" (echo ✅ package.json found) else echo ❌ package.json missing
if exist "node_modules" (echo ✅ Dependencies installed) else echo ⚠️  Dependencies not installed
if exist ".git" (echo ✅ Git repository initialized) else echo ❌ Git not initialized
echo.

pause
goto menu

:install_deps
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║           INSTALLING DEPENDENCIES           ║
echo ╚══════════════════════════════════════════════╝
echo.

if not exist "package.json" (
    echo ❌ No package.json found!
    pause
    goto menu
)

echo 📦 Installing dependencies...
npm install
if %errorlevel% equ 0 (
    echo ✅ Dependencies installed successfully!
) else (
    echo ❌ Installation failed
)
pause
goto menu

:pull_changes
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║            PULLING LATEST CHANGES           ║
echo ╚══════════════════════════════════════════════╝
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git not found!
    pause
    goto menu
)

if not exist ".git" (
    echo ❌ Not a Git repository!
    pause
    goto menu
)

echo 🔄 Pulling latest changes...
git pull origin main 2>nul || git pull origin master
if %errorlevel% equ 0 (
    echo ✅ Successfully pulled latest changes!
) else (
    echo ❌ Pull failed
)
pause
goto menu

:exit
cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║                GOODBYE!                      ║
echo ╚══════════════════════════════════════════════╝
echo.
echo 📚 Thanks for using Project Manager!
echo 🚀 Happy coding!
echo.
timeout /t 2 >nul
exit