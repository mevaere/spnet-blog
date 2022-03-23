@echo off
echo "Creation de l'environnement virtuel"
python -m pip install --upgrade pip
python -m venv venv
CALL .\venv\Scripts\activate
pip install -r requirements.txt
CALL .\make.bat html