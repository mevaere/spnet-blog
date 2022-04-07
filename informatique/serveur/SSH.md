---
orphan: true
---

# 🔐 SSH

## 🔑 Générer une paire de clé publique/privée

```bash
ssh-keygen -o -b 4096
sudo chmod 600 ~/.ssh/id_rsa
sudo chmod 600 ~/.ssh/id_rsa.pub
```

Vous pouvez ensuite transmettre la clé publique à votre hébergeur pour vous connecter sur votre instance.


## 🔗 Se connecter à votre instance

```bash
ssh -i ~/.ssh/id_rsa root@123.156.189.123 -p 12345
```

## 👨🏻‍💼 Créer un nouvel utilisateur (sudoable)

Création de l'utilisateur
```bash
adduser user_name
usermod -aG sudo user_name
```

Intégration de la clé
```bash
rsync --archive --chown=user_name:user_name ~/.ssh /home/user_name
```

Connexion possible maintenant depuis :

```bash
ssh -i ~/.ssh/id_rsa user_name@123.156.189.123 -p 12345
```

# 🛡 Protections supplémentaires

## SSHD

- Modification du port vers 12345 (ou autre)
- Autorisateur des utilisateurs pouvant se connecter sur SSH
- Interdiction de la connexion directe sans clé

```bash
sudo nano /etc/ssh/sshd_config
```

## 🔥 Parefeu

- On crée une règle **iptables** pour le pare-feu

```bash
sudo ufw allow 12345
sudo ufw enable
```
