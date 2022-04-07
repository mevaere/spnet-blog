---
orphan: true
---

# 🦄 Gunicorn et Django

## 🐍 Installation de Python

```bash
sudo apt install python3-pip python3-dev libpq-dev curl
```

- Environnement virtuel

```bash
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10-venv

mkdir ~/my_website
cd ~/my_website

python3.10 -m venv my_venv
source my_venv/bin/activate
python3.10 -m pip install --upgrade pip
```

## 💎 Installation de Django

```bash
pip install django gunicorn psycopg2-binary
```

- Créer un projet démo pour Django

```bash
django-admin startproject my_app ~/my_app
```

- On modifie les hôtes acceptés par Django settings

```python
import os
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . ., 'localhost']
```

- On lie la base de données (attention il ne faut pas mettre ces données en clair, l'idéal est de tout passer en variables d'environnement), mais ici il s'agit juste d'une démonstration de principe

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_app',
        'USER': 'remi',
        'PASSWORD': 'XXXXXXXXXXX',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

- Configuration du répertoire **static**, il faudra penser à configurer nginx pour directement distribuer ces fichiers

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

- Initialisation habituelle de Django

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

- On ouvre le port correspondant dans le pare-feu

```bash
sudo ufw allow 8000
python manage.py runserver 0.0.0.0:8000
```


## 🦄 Configuration de Gunicorn

```bash
cd ~/my_app
gunicorn --bind 0.0.0.0:8000 my_app.wsgi
```

- Nous pouvons sortir de notre environnement virtuel

```bash
deactivate
```

```bash
sudo nano /etc/systemd/system/gunicorn.socket
```

```bash
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

- On configure le service

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

```bash
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=spnet
Group=www-data
WorkingDirectory=/home/user_name/my_app
ExecStart=/home/user_name/my_app/my_venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          spnet.wsgi:application

[Install]
WantedBy=multi-user.target
```

- Utilisation en tant que service ensuite

```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

- Verification du fichier de socket

```bash
sudo systemctl status gunicorn.socket
```

```bash
file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket
```

```bash
sudo systemctl status gunicorn
```

```bash
curl --unix-socket /run/gunicorn.sock localhost
```

## 🗜 Nginx Proxy ➡ Gunicorn

```bash
sudo nano /etc/nginx/sites-available/my_app
```

```bash
server {
    listen 80;
    listen [::]:80;
    server_name xxx.xxx.xxx.xxx;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user_name/my_app;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```


```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled
```

- On peut supprimer le site par défaut aussi
- Si on veut une protection par passe (htpasswd)

```bash
sudo apt-get install apache2-utils
sudo htpasswd -c /etc/nginx/.htpasswd remi

auth_basic "Area 51";
auth_basic_user_file /etc/nginx/.htpasswd; 
```



```bash
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 80
```

```bash
sudo tail -F /var/log/nginx/error.log
```

```bash
sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql
sudo nginx -t && sudo systemctl restart nginx
```

- IP V6 sur Nginx (il suffit de rajouter) dans `/etc/nginx/sites-available/myapp`

```bash
# IPv4
listen :80;
# IPv6
listen [::]:80;
```

## 🔐 Ajout certificat SSL avec Let's Encrypt 

- Aucune difficulté particulière

```bash
sudo ufw allow 443
```

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d mon.site.fr
```
