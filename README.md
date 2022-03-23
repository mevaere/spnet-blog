# Installation du site Web

## Windows 🛠

1. Créer un nouveau répertoire **spnet** qui recueillera l'installateur
2. Télécharger les médias depuis [OneDrive](https://1drv.ms/u/s!AgJa84X1FzEptb43OYxI54SZN8fE2Q?e=r1G3h9)
3. Extraire les médias dans le repertoire **_medias**
4. Récupérer le fichier **_install.bat**
5. Lancer l'installateur


#### Contenu de l'installateur 💠
```bash
@echo off
echo "Installeur de SP.NET"
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
```

## Linux 🐧

*À proposer*

---
Par *Rémi MEVAERE* le *23 mars 2022*
