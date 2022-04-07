---
orphan: true
---

# 🌐 Serveur WEB Nginx avec Naxsi

Le but est de sécuriser Nginx avec le parefeu Naxsi WAF (Web Application Firewall)

## 🔩 Installation des logiciels nécessaires pour la compilation du serveur

```bash
sudo apt-get install libpcre3-dev libssl-dev libxml2-dev libxslt-dev libgd-dev libgeoip-dev zlib1g zlib1g-dev build-essential bzip2 unzip libpcre3-dev libssl-dev libgeoip-dev wget unzip libxslt-dev libgd-dev -y
```

## ℹ Récupération de la configuration avant compilation

Au choix :
- Vous gardez la version disponible sur Ubuntu Server
- Vous choisissez une version plus récente sur le site [Nginx](https://www.nginx.com/)

```bash
nginx -v
# nginx/1.18.0 (Ubuntu)
```

```bash
nginx -V
```

```bash
nginx version: nginx/1.18.0 (Ubuntu)
built with OpenSSL 1.1.1f  31 Mar 2020
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -fdebug-prefix-map=/build/nginx-KTLRnK/nginx-1.18.0=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-compat --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_image_filter_module=dynamic --with-http_sub_module --with-http_xslt_module=dynamic --with-stream=dynamic --with-stream_ssl_module --with-mail=dynamic --with-mail_ssl_module
```

## 🛠 Installation 

- Création du répertoire de travail

```bash
mkdir /tmp/naxsi 
cd /tmp/naxsi
```

- Téléchargement du logiciel et de naxsi (attention aux versions)

```bash
wget http://nginx.org/download/nginx-1.20.2.tar.gz
wget https://github.com/nbs-system/naxsi/archive/master.zip
tar -xvzf nginx-1.20.2.tar.gz
unzip master.zip
```

Il faudra ajouter la ligne suivante dans la configuration
```bash
ADD ./configure --add-module=/tmp/naxsi/naxsi-master/naxsi_src/
```

- Préparation à la compilation 

```bash
cd nginx-1.18.0
./configure --add-module=/tmp/naxsi/naxsi-master/naxsi_src/ --sbin-path=/usr/sbin/nginx --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-compat --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_image_filter_module=dynamic --with-http_sub_module --with-http_xslt_module=dynamic --with-stream=dynamic --with-stream_ssl_module --with-mail=dynamic --with-mail_ssl_module
```

- Installation

```bash
make
make install
sudo systemctl start nginx
nginx -V
```

- Blocage des maj depuis apt-get

```bash
sudo apt-mark hold nginx
```

- Copie des règles classiques de Naxsi

```bash
sudo cp /tmp/naxsi/naxsi-master/naxsi_config/naxsi_core.rules /etc/nginx
sudo nano /etc/nginx/nginx.conf
```

# Ajouter naxsi_core.rules dans la configuration de nginx.conf

```bash
sudo nano /etc/nginx/nginx.conf
# ---> include /etc/nginx/naxsi_core.rules;
```

Voici un exemple de règles pour mon site

```bash
sudo nano /etc/nginx/sciences-physiques.net.rules
```

```bash
# Sample rules file for vhost.
#LearningMode;
SecRulesEnabled;
#SecRulesDisabled;
DeniedUrl "/RequestDenied";

## check rules
CheckRule "$SQL >= 8" BLOCK;
CheckRule "$RFI >= 8" BLOCK;
CheckRule "$TRAVERSAL >= 4" BLOCK;
CheckRule "$EVADE >= 4" BLOCK;
CheckRule "$XSS >= 8" BLOCK;
error_log /var/log/nginx/sciences-physiques.net_log;
```

- Redémarrage du serveur

```bash
sudo service nginx restart
```
