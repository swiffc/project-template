@echo off
setlocal enabledelayedexpansion
title Project Manager v1.0
color 0A
:menu
cls
echo.
echo ================================================
echo              PROJECT MANAGER                 
echo           Development Toolkit                
echo ================================================
echo.
echo   1. Start Development Server
echo   2. Quick Commit (Version Number)
echo   3. Custom Commit Message
echo   4. View Git Status
echo   5. Project Info
echo   6. Install Dependencies
echo   7. Pull Latest Changes
echo   8. Setup .gitignore (Protect API Keys)
echo   9. Exit
echo.
echo ------------------------------------------------
set /p choice="Choose an option (1-9): "

if "%choice%"=="1" goto start_server
if "%choice%"=="2" goto quick_commit
if "%choice%"=="3" goto custom_commit
if "%choice%"=="4" goto git_status
if "%choice%"=="5" goto project_info
if "%choice%"=="6" goto install_deps
if "%choice%"=="7" goto pull_changes
if "%choice%"=="8" goto setup_gitignore
if "%choice%"=="9" goto exit
echo [ERROR] Invalid choice. Please select 1-9.
timeout /t 2 >nul
goto menu

:start_server
cls
echo.
echo ================================================
echo             STARTING DEV SERVER             
echo ================================================
echo.

where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js not found! Please install Node.js first.
    echo    Download from: https://nodejs.org/
    pause
    goto menu
)

where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] NPM not found! Please install Node.js first.
    pause
    goto menu
)

echo [OK] Node.js and NPM found
echo.

if not exist "package.json" (
    echo [ERROR] package.json not found!
    echo    Make sure you're in the project directory
    pause
    goto menu
)

echo [OK] Project files found
echo.

if not exist "node_modules" (
    echo [INFO] Installing dependencies...
    npm install
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to install dependencies
        pause
        goto menu
    )
    echo [OK] Dependencies installed
    echo.
)

set "start_cmd="
if exist "server\index.ts" set "start_cmd=npx tsx server/index.ts"
if exist "server\index.js" set "start_cmd=node server/index.js"
if exist "index.ts" set "start_cmd=npx tsx index.ts"
if exist "index.js" set "start_cmd=node index.js"

if "!start_cmd!"=="" (
    npm run dev >nul 2>&1
    if !errorlevel! equ 0 (
        set "start_cmd=npm run dev"
    ) else (
        echo [ERROR] No server entry point found!
        echo    Expected: server/index.ts, index.ts, or npm run dev
        pause
        goto menu
    )
)

netstat -an | findstr "127.0.0.1:5000" >nul
if %errorlevel% equ 0 (
    echo [WARN] Port 5000 may be in use
)

echo [INFO] Starting Development Server...
echo [INFO] Project: %CD%
echo.
echo ------------------------------------------------
echo Press Ctrl+C to stop server, then any key to return to menu
echo ------------------------------------------------
echo.

!start_cmd!
echo.
echo [INFO] Server stopped
pause
goto menu

:quick_commit
cls
echo.
echo ================================================
echo            QUICK VERSION COMMIT              
echo ================================================
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git not found! Please install Git first.
    echo    Download from: https://git-scm.com/
    pause
    goto menu
)

if not exist ".git" (
    echo [ERROR] Not a Git repository!
    echo    Initialize git with: git init
    pause
    goto menu
)

git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] No remote repository configured!
    echo    Add remote with: git remote add origin [url]
    pause
    goto menu
)

echo [OK] Git repository found
echo [INFO] Remote repository:
git remote get-url origin
echo.

echo [INFO] Current changes:
git status --porcelain
echo.
echo ------------------------------------------------
set /p version="Enter version (e.g., v1.0, v1.1, v2.0): "

if "!version!"=="" (
    echo [ERROR] No version entered
    timeout /t 2 >nul
    goto menu
)

echo.
echo [INFO] Adding all changes...
git add .
if !errorlevel! neq 0 (
    echo [ERROR] Failed to add changes
    pause
    goto menu
)

echo [INFO] Committing as !version!...
git commit -m "!version!"
if !errorlevel! neq 0 (
    echo [ERROR] Commit failed (no changes or error)
    pause
    goto menu
)

echo [INFO] Pushing to repository...
git push origin main >nul 2>&1
if !errorlevel! neq 0 (
    git push origin master >nul 2>&1
    if !errorlevel! neq 0 (
        echo [ERROR] Push failed - check network/credentials
        pause
        goto menu
    )
)

echo.
echo [SUCCESS] Successfully committed and pushed !version!!
echo [INFO] Changes are now live on repository
timeout /t 3 >nul
goto menu

:custom_commit
cls
echo.
echo ================================================
echo           CUSTOM COMMIT MESSAGE             
echo ================================================
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git not found!
    pause
    goto menu
)

if not exist ".git" (
    echo [ERROR] Not a Git repository!
    pause
    goto menu
)

echo [INFO] Current changes:
git status --short
echo.
echo ------------------------------------------------

:input_message
set /p message="Enter commit message: "
if "!message!"=="" (
    echo [ERROR] Message cannot be empty
    goto input_message
)

echo.
echo [INFO] Adding changes...
git add .

echo [INFO] Committing: "!message!"
git commit -m "!message!"
if !errorlevel! neq 0 (
    echo [ERROR] Commit failed
    pause
    goto menu
)

echo [INFO] Pushing to repository...
git push origin main >nul 2>&1
if !errorlevel! neq 0 (
    git push origin master >nul 2>&1
    if !errorlevel! neq 0 (
        echo [ERROR] Push failed - check connection
        pause
        goto menu
    )
)

echo.
echo [SUCCESS] Successfully committed and pushed!
timeout /t 3 >nul
goto menu

:git_status
cls
echo.
echo ================================================
echo              GIT STATUS REPORT               
echo ================================================
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git not installed
    pause
    goto menu
)

if not exist ".git" (
    echo [ERROR] Not a Git repository
    pause
    goto menu
)

echo [INFO] Repository Information:
git remote get-url origin 2>nul
echo.

echo [INFO] Current Branch:
git branch --show-current
echo.

echo [INFO] Working Directory Status:
git status --short
echo.

echo [INFO] Recent Commits (Last 5):
git log --oneline -5 --decorate
echo.

pause
goto menu

:project_info
cls
echo.
echo ================================================
echo             PROJECT INFORMATION              
echo ================================================
echo.

echo [INFO] System Information:
echo ------------------------------------------------
echo Directory: %CD%
echo User: %USERNAME%
echo Date/Time: %DATE% %TIME%
echo.

echo [INFO] Environment Check:
where node >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Node.js installed:
    node --version
) else (
    echo [ERROR] Node.js: Not installed
)

where npm >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] NPM installed:
    npm --version
) else (
    echo [ERROR] NPM: Not installed
)

where git >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Git installed:
    git --version
) else (
    echo [ERROR] Git: Not installed
)

echo.

echo [INFO] Project Files:
if exist "package.json" (echo [OK] package.json found) else echo [ERROR] package.json missing
if exist "node_modules" (echo [OK] Dependencies installed) else echo [WARN] Dependencies not installed
if exist ".git" (echo [OK] Git repository initialized) else echo [ERROR] Git not initialized
if exist ".gitignore" (echo [OK] .gitignore configured) else echo [WARN] .gitignore missing
echo.

pause
goto menu

:install_deps
cls
echo.
echo ================================================
echo           INSTALLING DEPENDENCIES           
echo ================================================
echo.

if not exist "package.json" (
    echo [ERROR] No package.json found!
    pause
    goto menu
)

echo [INFO] Installing dependencies...
npm install
if %errorlevel% equ 0 (
    echo [SUCCESS] Dependencies installed successfully!
) else (
    echo [ERROR] Installation failed
)
pause
goto menu

:pull_changes
cls
echo.
echo ================================================
echo            PULLING LATEST CHANGES           
echo ================================================
echo.

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git not found!
    pause
    goto menu
)

if not exist ".git" (
    echo [ERROR] Not a Git repository!
    pause
    goto menu
)

echo [INFO] Pulling latest changes...
git pull origin main >nul 2>&1
if %errorlevel% neq 0 (
    git pull origin master >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERROR] Pull failed
        pause
        goto menu
    )
)

echo [SUCCESS] Successfully pulled latest changes!
pause
goto menu

:setup_gitignore
cls
echo.
echo ================================================
echo           SETUP .GITIGNORE FILE           
echo ================================================
echo.

if exist ".gitignore" (
    echo [INFO] .gitignore already exists
    echo [WARN] File will be overwritten
    set /p overwrite="Continue and overwrite? (y/n): "
    if not "!overwrite!"=="y" if not "!overwrite!"=="Y" goto menu
)

echo [INFO] Creating comprehensive .gitignore file...

echo # Environment Variables > .gitignore
echo .env >> .gitignore
echo .env.local >> .gitignore
echo .env.development >> .gitignore
echo .env.test >> .gitignore
echo .env.production >> .gitignore
echo .env.staging >> .gitignore
echo. >> .gitignore
echo # API Keys and Secrets >> .gitignore
echo *.key >> .gitignore
echo *.pem >> .gitignore
echo config/secrets.json >> .gitignore
echo secrets/ >> .gitignore
echo. >> .gitignore
echo # Dependencies >> .gitignore
echo node_modules/ >> .gitignore
echo npm-debug.log* >> .gitignore
echo yarn-debug.log* >> .gitignore
echo yarn-error.log* >> .gitignore
echo. >> .gitignore
echo # Build outputs >> .gitignore
echo dist/ >> .gitignore
echo build/ >> .gitignore
echo out/ >> .gitignore
echo .next/ >> .gitignore
echo. >> .gitignore
echo # Cache directories >> .gitignore
echo .cache/ >> .gitignore
echo .parcel-cache/ >> .gitignore
echo .vite/ >> .gitignore
echo. >> .gitignore
echo # OS generated files >> .gitignore
echo .DS_Store >> .gitignore
echo .DS_Store? >> .gitignore
echo ._* >> .gitignore
echo .Spotlight-V100 >> .gitignore
echo .Trashes >> .gitignore
echo ehthumbs.db >> .gitignore
echo Thumbs.db >> .gitignore
echo. >> .gitignore
echo # IDE files >> .gitignore
echo .vscode/ >> .gitignore
echo .idea/ >> .gitignore
echo *.swp >> .gitignore
echo *.swo >> .gitignore
echo *~ >> .gitignore
echo. >> .gitignore
echo # Logs >> .gitignore
echo logs/ >> .gitignore
echo *.log >> .gitignore
echo. >> .gitignore
echo # Runtime data >> .gitignore
echo pids/ >> .gitignore
echo *.pid >> .gitignore
echo *.seed >> .gitignore
echo *.pid.lock >> .gitignore
echo. >> .gitignore
echo # Coverage directory >> .gitignore
echo coverage/ >> .gitignore
echo .nyc_output/ >> .gitignore
echo. >> .gitignore
echo # Database >> .gitignore
echo *.db >> .gitignore
echo *.sqlite >> .gitignore
echo *.sqlite3 >> .gitignore
echo. >> .gitignore
echo # Temporary folders >> .gitignore
echo tmp/ >> .gitignore
echo temp/ >> .gitignore
echo. >> .gitignore
echo # Optional npm cache >> .gitignore
echo .npm >> .gitignore
echo. >> .gitignore
echo # Optional REPL history >> .gitignore
echo .node_repl_history >> .gitignore

if %errorlevel% equ 0 (
    echo [SUCCESS] .gitignore file created successfully!
    echo.
    echo [SECURITY] Your API keys and environment variables are now protected:
    echo - .env files will not be committed to Git
    echo - API keys in *.key files are excluded
    echo - secrets/ folder is ignored
    echo - All sensitive data patterns are covered
    echo.
    
    if not exist ".env.example" (
        echo [INFO] Creating .env.example template...
        echo # Environment Variables Template > .env.example
        echo # Copy this file to .env and fill in your actual values >> .env.example
        echo. >> .env.example
        echo # Database >> .env.example
        echo DATABASE_URL=your_database_url_here >> .env.example
        echo. >> .env.example
        echo # API Keys >> .env.example
        echo OPENAI_API_KEY=your_openai_key_here >> .env.example
        echo STRIPE_SECRET_KEY=your_stripe_key_here >> .env.example
        echo. >> .env.example
        echo # Server Configuration >> .env.example
        echo PORT=5000 >> .env.example
        echo NODE_ENV=development >> .env.example
        echo [SUCCESS] Created .env.example template file
    )
    
    if exist ".env" (
        git ls-files --error-unmatch .env >nul 2>&1
        if !errorlevel! equ 0 (
            echo [CRITICAL] .env file is currently tracked by Git!
            echo [ACTION] Removing .env from Git tracking...
            git rm --cached .env >nul 2>&1
            if !errorlevel! equ 0 (
                echo [SUCCESS] .env removed from Git tracking
            ) else (
                echo [WARN] Could not remove .env from Git tracking
            )
        )
    )
    
) else (
    echo [ERROR] Failed to create .gitignore file
)

pause
goto menu

:exit
cls
echo.
echo ================================================
echo                GOODBYE!                      
echo ================================================
echo.
echo Thanks for using Project Manager!
echo Happy coding!
echo.
timeout /t 2 >nul
exit