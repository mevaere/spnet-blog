@echo off
git checkout main
git fetch origin
git reset --hard origin/main
CALL .\venv\Scripts\activate
CALL .\make.bat clean
CALL .\make.bat html
