---
orphan: true
---

# 📬 Postfix

Le but est de configurer postfix comme serveur SMTP local pour envoyer des mails vers l'extérieur.

## 🔩 Installation

```bash
sudo apt-get update
# choix - internet puis fqdn sciences-physiques.net pour moi
sudo apt-get install postfix -y
sudo apt install mailutils
```

## 🛠 Configuration

- Attention il est **INDISPENSABLE** pour avoir un score de 10/10 sur mail-tester et ne pas se faire jeter par Google d'avoir un `reverse DNS` configuré sur votre hostname !
- Ici l'adresse IP de mon serveur pointe vers `mail.sciences-physiques.net`
- Il faut aussi ouvrir une zone de *type A* dans votre configuration DNS

```bash
sudo postconf -e "myhostname = mail.sciences-physiques.net"
sudo postconf -e "mydomain = sciences-physiques.net"
sudo postconf -e "smtp_tls_security_level = may"
sudo postconf -e "smtp_tls_loglevel = 1"
sudo postconf -e "inet_protocols = ipv4"
```

- Vérification

```bash
postconf mydomain
```

- Configuration de /etc/mailname

```bash
echo "sciences-physiques.net" | sudo tee /etc/mailname
```

```bash
sudo nano /etc/postfix/main.cf

---> inet_interfaces = loopback-only
---> mydestination = localhost.$mydomain, localhost, $myhostname
---> append_dot_mydomain = yes

sudo systemctl restart postfix
```

- Tester le fonctionnement du serveur en envoyant un mail

```bash
Test

echo "Bonjour" | mail -s "C'est un test" destinataire@adres.se -aFrom:expediteur@adres.se
```

- Sinon lire le log
```bash
sudo tail /var/log/mail.log
```

- Obtenir un certificat SSL pour sécuriser les connexions entre serveur SMTP (et ne pas se faire jeter)


```bash
sudo certbot certonly --standalone -d sciences-physiques.net
```

## 🔐 OpenDkim

- Installation des outils

```bash
sudo apt-get install opendkim opendkim-tools -y
sudo adduser postfix opendkim
```

- Procéder aux changements suivants

```bash
sudo nano /etc/opendkim.conf
```

```bash
Canonicalization     relaxed/simple
Mode                 s
SubDomains           no
```

```bash
# Map domains in From addresses to keys used to sign messages
KeyTable           refile:/etc/opendkim/key.table
SigningTable       refile:/etc/opendkim/signing.table
```

```bash
sudo mkdir /etc/opendkim
sudo mkdir /etc/opendkim/keys
sudo chown -R opendkim:opendkim /etc/opendkim
sudo chmod go-rw /etc/opendkim/keys
```

- Ajout des tables pour mon nom de domain

```bash
sudo nano /etc/opendkim/signing.table
```

```bash
*@sciences-physiques.net     sendonly._domainkey.sciences-physiques.net
```

- Création des tables

Create table

```bash
sudo nano /etc/opendkim/key.table
```

```bash
sendonly._domainkey.sciences-physiques.net    sciences-physiques.net:sendonly:/etc/opendkim/keys/sciences-physiques.net/sendonly.private
```

- Création des clés

```bash
sudo nano /etc/opendkim/trusted.hosts
```

```bash
127.0.0.1
localhost

*.sciences-physiques.net
```

```bash
sudo mkdir /etc/opendkim/keys/sciences-physiques.net
sudo opendkim-genkey -b 2048 -d sciences-physiques.net -D /etc/opendkim/keys/sciences-physiques.net -s sendonly -v
```

```bash
sudo chown opendkim:opendkim /etc/opendkim/keys/sciences-physiques.net/sendonly.private
```

- Afficher la clé

```bash
sudo cat /etc/opendkim/keys/sciences-physiques.net/sendonly.txt
```

- Tester le fonctionnement de la clé avant ajout dans la bonne zone DNS

```bash
sudo opendkim-testkey -d sciences-physiques.net -s sendonly -vvv
```

## 🔗 Faire le lien avec Postfix

```bash
sudo nano /etc/opendkim.conf
```

- Remplacer

`Socket local:/var/run/postfix/opendkim/opendkim.sock` par `Socket local:/var/spool/postfix/opendkim/opendkim.sock`

- Modification des autorisations

```bash
sudo mkdir /var/spool/postfix/opendkim
sudo chown opendkim:postfix /var/spool/postfix/opendkim
```


-Si vous ne trouvez pas la ligne suivante dans le fichier `/etc/default/opendkim`.

```bash
SOCKET="local:/var/run/opendkim/opendkim.sock"
# ou
SOCKET=local:$RUNDIR/opendkim.sock
```

- Changer par 

```bash
SOCKET="local:/var/spool/postfix/opendkim/opendkim.sock"
```

- Configuration de postfix

```bash
sudo nano /etc/postfix/main.cf
```

```bash
milter_default_action = accept
milter_protocol = 6
smtpd_milters = local:opendkim/opendkim.sock
non_smtpd_milters = $smtpd_milters
```

## 🔑 Créer une zone SPF dans les DNS

```{hint}
Le SPF (Sender Policy Framework) est un système de validation par courrier électronique pour empêcher les spammeurs d'envoyer des messages au nom de votre domaine. Avec le SPF, une organisation peut publier des serveurs de messagerie autorisés.

```


```bash
TXT  @   v=spf1 mx ip4:xxx.xxx.xxx.xxx ip6:xxxx:xxxx::xxxx:xxxx:xxxx:xxxx ~all
```

## 💣 Créer une zone DMARC dans les DNS

```{hint}
DMARC est un protocole ouvert d'authentification du courrier électronique qui assure la protection du canal de courrier électronique au niveau du domaine. L'authentification DMARC détecte et empêche les techniques d'usurpation de courrier électronique utilisées dans le phishing, la compromission du courrier électronique professionnel (BEC) et d'autres attaques basées sur le courrier électronique. S'appuyant sur les normes existantes, SPF et DKIM, DMARC est la première et la seule technologie largement déployée qui peut rendre l'en-tête “from” domain fiable. Le propriétaire du domaine peut publier un enregistrement DMARC dans le système de noms de domaine (DNS) et créer une politique pour dire aux destinataires ce qu'ils doivent faire des courriels dont l'authentification échoue.
```

```bash
v=DMARC1; p=reject; rua=; ruf=; fo=1; pct=100; adkim=s; aspf=s
```


## 🧪 Tester sur [Mail-Tester](https://www.mail-tester.com/)

```{image} ../../_medias/informatique/serveur/mailtester.png
:width: 400px
:target: https://www.mail-tester.com/
:align: center
```
