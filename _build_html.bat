@echo off
git checkout main
git pull
git reset --hard
CALL .\venv\Scripts\activate
CALL .\make.bat html