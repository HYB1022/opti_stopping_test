@echo off
chcp 65001 > nul

echo Cleaning...

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__

echo Building...

pyinstaller ^
--onefile ^
--clean ^
--collect-all matplotlib ^
--icon=icon.ico ^
--name OptimalStopping ^
--upx-dir=upx ^
main.py

echo.
echo Done!
pause