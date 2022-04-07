# 🐧 Serveur Ubuntu 18.04

Vous trouverez ci-dessous un résumé des différentes *notes* gardées pour mettre en place un serveur Ubuntu exécutant Django. Peut-être certains trouveront cela utile.  

## ✨ Préliminaires

- Mettre à jour le système

```bash
sudo apt-get update -y & sudo apt-get upgrade -y
sudo apt update -y & sudo apt upgrade -y 
sudo apt-get dist-upgrade
sudo apt-get autoremove --purge -y
sudo apt autoremove --purge -y
sudo reboot
```

- Choisir la bonne zone horaire pour votre serveur (ça peut servir)

```bash
sudo timedatectl set-timezone Europe/Paris
```

## 🛡 Accès SSH et sécurité

* [](serveur/SSH)

## 🧩 Logiciels à installer

* [](serveur/postgresql)
* [](serveur/nginx)
* [](serveur/gunicorn)
* [](serveur/postfix)

## 🦺 Backup, maintenance

* [](serveur/backup)
* [](serveur/nmon) 
