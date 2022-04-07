---
orphan: true
---

# 👓 Nmon

L'outil [Nmon](http://nmon.sourceforge.net/) permet de suivre les performances du serveur pour savoir s'il faut l'upscaler ou non.

## 🧩 Installation


| ![Image 1](../../_medias/informatique/serveur/nmon.gif)
|:--:| 
| Le logiciel Nmon récolte des informations sur le fonctionnement du serveur |


```bash
sudo apt-get install nmon
sudo mkdir /var/log/nmon
sudo chown root:root /var/log/nmon
sudo chmod 775 /var/log/nmon
```

- Tous les jours

```bash
crontab -e 
0 0 * * * nmon -m /var/log/nmon -f -s 60 -c 1440 >/dev/null 2>&1
```
- Il faut configurer un logrotate pour éviter l'accumulation des logs

## 📊 Utilisation

- J'utilise [Nmon Visualizer](https://nmonvisualizer.github.io/nmonvisualizer/)


| ![Image 1](../../_medias/informatique/serveur/analyser.jpg)
|:--:| 
| Nmon Visualizer est un logiciel qui permet d'afficher les données récoltées |
