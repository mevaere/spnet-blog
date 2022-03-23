@echo off
set file=%0
FOR %%i IN ("%file%") DO (set filename=%%~ni)
if %filename% == buffer_install (
git init .
git remote add origin https://github.com/mevaere/spnet.git
git pull origin main
git branch -m main
git branch --set-upstream-to origin/main
python -m pip install --upgrade pip
python -m venv venv
CALL .\venv\Scripts\activate
pip install -r requirements.txt
CALL .\make.bat html
deactivate
del buffer_install.bat
exit
) ELSE (
copy _install.bat buffer_install.bat
start buffer_install.bat
del _install.bat
)