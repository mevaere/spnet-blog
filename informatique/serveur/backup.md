---
orphan: true
---

# 🦺 Backup

## 🗜 Monter un S3 avec S3fuse

Le tutoriel se base sur mon expérience chez Scaleway France.

### Compilation

```bash
apt update && apt upgrade -y
apt -y install automake autotools-dev fuse g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
```

```bash
cd /tmp
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse
```

- Mettre à jour la valeur `MAX_MULTIPART_CNT` dans le fichier `fdcache.cpp`

```bash
sed -i 's/MAX_MULTIPART_CNT = 10 /MAX_MULTIPART_CNT = 1 /' src/fdcache.cpp
```

- Compilation avec g++

```bash
./autogen.sh
./configure
make
make install
```

- Copie de l'application

```bash
cp src/s3fs /usr/local/bin/s3fs
```

### Configuration du montage

- On ouvre une session sur l'utilisateur qui nous intéresse

```bash
echo MONMOTDEPASSE > $HOME/.passwd-s3fs
chmod 600 $HOME/.passwd-s3fs
```

- On crée le répertoire qui servira au montage

```bash
cd /mnt
mkdir spnet-bucker
chmod 770 spnet-bucket
```

- On monte le répertoire avec s3fuse

```bash
s3fs spnet-bucket /mnt/spnet-bucket -o allow_other -o passwd_file=/root/.passwd-s3fs -o use_path_request_style -o endpoint=fr-par -o parallel_count=15 -o multipart_size=128 -o nocopyapi -o url=https://s3.fr-par.scw.cloud
```

### Montage automatique au démarrage

- On ouvre `/etc/fstab`

```bash
sudo nano /etc/fstab
```

- On ajoute la ligne suivante

```bash
s3fs#spnet-bucket /mnt/spnet-bucket fuse _netdev,allow_other,use_path_request_style,url=https://s3.fr-par.scw.cloud/ 0 0
```


## 📦 BackupManager

### 🔑 Remarques sur GPG

```{hint}
GnuPG (ou GPG, de l'anglais GNU Privacy Guard) est l'implémentation GNU du standard OpenPGP défini dans la RFC 48806, distribuée selon les termes de la licence publique générale GNU.
Ce logiciel permet la transmission de messages électroniques signés et chiffrés, garantissant ainsi leurs authenticité, intégrité et confidentialité. 

```

```bash
sudo apt update
sudo apt install gnupg

```

#### Créer une paire de clés

```bash
gpg --gen-key

```

#### Lister les clés

```bash
gpg --list-keys
gpg --list-secret-keys

```

#### Exporter les clés

```bash
gpg --output public_key.pgp --armor --export webmaster@sciences-physiques.net
gpg --output private.pgp --armor --export-secret-key webmaster@sciences-physiques.net

```

#### Chiffrer/Déchiffrer fichiers

```bash
gpg --encrypt --recipient 'admin@example.com' --output confidential.txt.enc public.txt

```

```bash
gpg --decrypt --output public.txt confidential.txt.enc

```


### BackupManager

- Installation

```bash
sudo apt-get update
sudo apt-get install backup-manager -y
```

- Configuration

```bash
sudo nano /etc/backup-manager.conf
```

## 🐘 Utiliser pgbackrest pour sauvegarder la base de données

### Préliminaires

```bash
sudo apt-get install postgresql-client libxml2
```

### Compilation de pgbackrest

```bash
cd /tmp
mkdir -p /build
wget -q -O - https://github.com/pgbackrest/pgbackrest/archive/release/2.36.tar.gz |  tar zx -C /build

sudo apt-get install make gcc libpq-dev libssl-dev libxml2-dev pkg-config liblz4-dev libzstd-dev libbz2-dev libz-dev libyaml-dev
cd /build/pgbackrest-release-2.36/src && ./configure && make
cp pgbackrest /usr/bin
sudo chmod 755 /usr/bin/pgbackrest
```

### Permissions

```bash
sudo mkdir -p -m 770 /var/log/pgbackrest
sudo chown postgres:postgres /var/log/pgbackrest
sudo mkdir -p /etc/pgbackrest
sudo mkdir -p /etc/pgbackrest/conf.d
sudo touch /etc/pgbackrest/pgbackrest.conf
sudo chmod 640 /etc/pgbackrest/pgbackrest.conf
sudo chown postgres:postgres /etc/pgbackrest/pgbackrest.conf
```

### Test installation

```bash
sudo -u postgres pgbackrest
```

```bash
cat /etc/postgresql/12/main/postgresql.conf
```

### Configuration

```bash
sudo nano /etc/pgbackrest/pgbackrest.conf
```

```bash
[main]
pg1-path=/var/lib/postgresql/12/main

[global]
repo1-cipher-pass=VOTRE_PASS_ICI
repo1-cipher-type=aes-256-cbc
repo1-path=/var/lib/pgbackrest
repo1-retention-full=15
start-fast=y

[global:archive-push]
compress-level=3

```

### Path des logs

```bash
sudo -u postgres bash -c ' \
       export PGBACKREST_LOG_PATH=/var/log/pgbackrest && \
       pgbackrest --log-level-console=error help backup log-path'
```

### Créer les repositories

```bash
rm -rf /var/lib/pgbackrest
rm -rf /mnt/spnet-bucket/pgbackrest

sudo mkdir -p /var/lib/pgbackrest
sudo chmod 750 /var/lib/pgbackrest
sudo chown postgres:postgres /var/lib/pgbackrest
sudo mkdir -p /mnt/spnet-bucket/pgbackrest
sudo chmod 775 /mnt/spnet-bucket/pgbackrest

```

### Configuration des archives

```bash
sudo nano /etc/postgresql/14/main/postgresql.conf
```

```bash
archive_command = 'pgbackrest --stanza=main archive-push %p'
archive_mode = on
listen_addresses = 'localhost'
log_line_prefix = ''
max_wal_senders = 3
wal_level = replica
```

### Redémarrage

```bash
sudo pg_ctlcluster 14 main restart
```

### Créer un stranza

```bash
sudo -u postgres pgbackrest --stanza=main --log-level-console=info stanza-create
```

### Vérification

```bash
sudo -u postgres pgbackrest --stanza=main --log-level-console=info check
```

### Créer une sauvegarde

```bash
sudo -u postgres pgbackrest --stanza=main --type=full --log-level-console=error backup
```

### Taille d'une sauvegarde

```bash
du -h /var/lib/pgbackrest -d 1
```

### Information sur une sauvegarde

```bash
sudo -u postgres pgbackrest info
```

### Restaurer une sauvegarde

```bash
sudo pg_ctlcluster 14 main stop
sudo -u postgres find /var/lib/postgresql/14/main -mindepth 1 -delete
sudo -u postgres pgbackrest --stanza=main --set=20211218-143625F restore
sudo pg_ctlcluster 14 main start
```

## 📜 Script perso pour la sauvegarde et la restauration

### Envoyer vers S3Fuse

```bash

cd /tmp/
sudo -u postgres pgbackrest --stanza=main --type=full --log-level-console=error backup
now=$(date +"%Y_%m_%d-%H_%M")
year=$(date +"%Y")
month=$(date +"%m")
cd /var/lib/pgbackrest 
tar -cf /tmp/pgback-${now}.tar *
cd /tmp/
xz -9 -c /tmp/pgback-${now}.tar > /tmp/pgback-${now}.tar.xz
sudo -H -u postgres bash -c "pg_dumpall -c > /tmp/${now}.psql"
xz -9 -c /tmp/${now}.psql > /tmp/${now}.psql.xz
gpg --output /tmp/${now}.psql.gpg --encrypt --recipient xxxxx@sciences-physiques.net /tmp/${now}.psql
gpg --output /tmp/pgback-${now}.tar.xz.gpg --encrypt --recipient xxxxx@sciences-physiques.net /tmp/pgback-${now}.tar.xz
rm -rf /var/archives/*
backup-manager
cd /var/archives 
tar -cf /tmp/backup-manager-${now}.tar *
cd /tmp/
xz -9 -c /tmp/backup-manager-${now}.tar > /tmp/backup-manager-${now}.tar.xz
gpg --output /tmp/backup-manager-${now}.tar.xz.gpg --encrypt --recipient xxxxx@sciences-physiques.net /tmp/backup-manager-${now}.tar.xz
rm /tmp/pgback-${now}.tar
rm /tmp/${now}.psql
rm /tmp/${now}.psql.xz
rm /tmp/pgback-${now}.tar.xz
rm /tmp/backup-manager-${now}.tar
rm /tmp/backup-manager-${now}.tar.xz
sudo mkdir -p /mnt/spnet-bucket/${year}/${month}/
mv /tmp/*${now}.tar.xz.gpg /mnt/spnet-bucket/${year}/${month}/
```

### Restauration

```bash

rm -rf /var/lib/pgbackrest
sudo mkdir -p /var/lib/pgbackrest
sudo chmod 750 /var/lib/pgbackrest
sudo chown postgres:postgres /var/lib/pgbackrest
tar -Pxf *.tar.xz -C /var/lib/pgbackrest
```

## Quelques commandes utiles

### Restaurer une base de données

```bash
pg_dumpall -c > remi_ok.sql
psql -U postgres -f remi_ok.sql
```

### Déchiffrer un fichier

```bash
gpg --output /tmp/decrypt.tar.xz --decrypt /tmp/bm.tar.xz.gpg
```

### Extraire un fichier .xz

```bash
tar -xf decrypt.tar.xz -C /tmp/extract
```

### Copier des fichiers de manière récursive


```bash
cp -R <source_folder>/* <destination_folder>
```
