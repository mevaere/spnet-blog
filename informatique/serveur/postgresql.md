---
orphan: true
---

# 🗄 PostgreSQL

## 🔩 Préliminaires

- Pour une version plus récente de PostgreSQL

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt -y update
sudo apt -y install postgresql-14
```

## Mise à jour 

```bash
sudo systemctl stop postgresql.service
sudo su - postgres

/usr/lib/postgresql/14/bin/pg_upgrade \
  --old-datadir=/var/lib/postgresql/12/main \
  --new-datadir=/var/lib/postgresql/14/main \
  --old-bindir=/usr/lib/postgresql/12/bin \
  --new-bindir=/usr/lib/postgresql/14/bin \
  --old-options '-c config_file=/etc/postgresql/12/main/postgresql.conf' \
  --new-options '-c config_file=/etc/postgresql/14/main/postgresql.conf' \
  --check

/usr/lib/postgresql/14/bin/pg_upgrade \
  --old-datadir=/var/lib/postgresql/12/main \
  --new-datadir=/var/lib/postgresql/14/main \
  --old-bindir=/usr/lib/postgresql/12/bin \
  --new-bindir=/usr/lib/postgresql/14/bin \
  --old-options '-c config_file=/etc/postgresql/12/main/postgresql.conf' \
  --new-options '-c config_file=/etc/postgresql/14/main/postgresql.conf'

exit
```

## Mise à jour des autorisations

```bash
sudo nano /etc/postgresql/14/main/postgresql.conf
# ...and change "port = 5433" to "port = 5432"

sudo nano /etc/postgresql/12/main/postgresql.conf
# ...and change "port = 5432" to "port = 5433"

sudo systemctl start postgresql.service
sudo su - postgres

/usr/lib/postgresql/14/bin/vacuumdb --all --analyze-in-stages

# Update passwords
psql
\du
\password user
\q
exit

# Create a superuser

CREATE ROLE root-ps WITH LOGIN SUPERUSER PASSWORD 'pass';

#delete old
apt list --installed | grep postgresql
sudo apt-get remove postgresql-12
sudo rm -rf /etc/postgresql/12/
./delete_old_cluster.sh
```

```bash
sudo -u postgres psql
```

```guess
CREATE DATABASE DBB_NAME;
CREATE USER remi WITH PASSWORD 'XXXXXXXXXXXXXXXXXXXXXXXXXX';
ALTER ROLE remi SET client_encoding TO 'utf8';
ALTER ROLE remi SET default_transaction_isolation TO 'read committed';
ALTER ROLE remi SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE DBB_NAME TO remi;
\q
```

## Configure PostgreSQL

- Récupérer les configurations sur [PGTune](https://pgtune.leopard.in.ua/)

```{image} ../../_medias/informatique/serveur/pgtune.png
:width: 400px
:target: https://pgtune.leopard.in.ua/
:align: center
```

```bash
sudo nano /etc/postgresql/14/main/postgresql.conf
sudo systemctl restart postgresql
```
