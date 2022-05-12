# 📷 Portfolio

## 🔭 SP.NET


```{image} ../_medias/spnet-app/home_tb.png
:width: 350px
:target: ../_static/spnet-app/home.png
:align: center
```

<br>

### 📑 Description
```{eval-rst}
:Projet: Sciences-Physiques.NET
:Langage: Python 3.10
:Back-end: Django Framework
:Front-end: HTML / CSS
:Testing: unittest
:Année: 2022
:Description: Logiciel permettant la commande, la gestion et le suivi des cours en groupe de sciences physiques et chimiques dispensés sur Zoom et disponible en VOD sur Vimeo. L'objectif est d'avoir un cadre stable et un système totalement automatisé. 
:Statut: Annulé pour des raisons juridiques

```

### 🛠 Fonctionnalités
```{eval-rst}
:Utilisateurs: Gestion des utilisateurs
:Zoom API: Inscription automatique aux meetings Zoom
:Vimeo: Accès automatique aux vidéos Zoom
:Stripe API: Gestion des paiements / remboursement par Stripe
:Todoist API: Gestion SAV, communication interne par Todoist
:Task Manager: Programme Python autonome pour les appels API
:Error Manager: Gestion au maximum des erreurs pour éviter intervention manuelle
:Statistiques: Production de statistiques détaillées
:Newsletter: Création de newsletters personnalisées en fonction des élèves
:Courriel: Production et transmission des courriels sans service tiers - **mail-tester.com 10/10**
:Facturation: Facturation et comptabilité automatique
:Stripe: Remboursement automatique en cas d'annulation
:Sécurisation: Evite le partage de cours, IP
:Anti-Bot: Intégration recaptcha V3 de Google

```


### ⌨ Serveur
```{eval-rst}
:Server: Ubuntu Server 18.04
:Database: PostgreSQL
:DBB Backup: pgbackrest
:Hosting: Scaleway France
:Web Server: Nginx / Gunicorn
:SSL: Let's Encrypt
:Protection: Naxsi
:SMTP server: Postfix with DKIM
:Backup Tool: S3fuse, BackupManager, scripts persos
:Sysop: Nmon

```

### 🖼 Screenshots


```{image} ../_medias/spnet-app/basket_tb.png
:target: ../_static/spnet-app/basket.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/codecoverage_tb.png
:target: ../_static/spnet-app/codecoverage.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/connexion_tb.png
:target: ../_static/spnet-app/connexion.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/contacts_tb.png
:target: ../_static/spnet-app/contacts.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/courses_tb.png
:target: ../_static/spnet-app/courses.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/infos_tb.png
:target: ../_static/spnet-app/infos.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/orders_tb.png
:target: ../_static/spnet-app/orders.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/responsive_tb.png
:target: ../_static/spnet-app/responsive.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/shopping_tb.png
:target: ../_static/spnet-app/shopping.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/shopping2_tb.png
:target: ../_static/spnet-app/shopping2.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/stripe_tb.png
:target: ../_static/spnet-app/stripe.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/task_scheduler_tb.png
:target: ../_static/spnet-app/task_scheduler.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/unittest_tb.png
:target: ../_static/spnet-app/unittest.png
:align: center
```

<br>

```{image} ../_medias/spnet-app/videos_tb.png
:target: ../_static/spnet-app/videos.png
:align: center
```

## 💌 Client Mail Checker


```{image} ../_medias/a_propos/cp_cmc.gif
:width: 400px
:target: None
:align: center
```


### 📑 Description

```{eval-rst}
:Projet: Client Mail complet (POP/IMAP/SMTP)
:Langage: Pascal Object (Delphi)
:Année: 2004
:Statut: Obsolète

```

### 📣 Interview (verbatim)

````{admonition} Interview
```{image} ../_medias/a_propos/cmc-remimevaere.jpg
:align: center
```
Rémi Mévaere, 17 ans, est étudiant au lycée Angellier à Dunkerque. Il est l’heureux concepteur de Client Mail Checker, logiciel de messagerie original lancé en avril 2004 et déjà téléchargé à 8000 exemplaires. Ses objectifs immédiats : finir son année de terminale, avec une bonne mention au bac. Puis rentrer à l’INSA de Lyon ou à l’ENSIMAG de Grenoble. Pour intégrer ensuite une société en tant que chef de projet. Interview.

**Pourquoi vous êtes-vous lancé dans la conception d’un logiciel de messagerie ?**
Utilisant beaucoup les mails en tant que webmaster, j’avais besoin d’un outil personnalisé qui répondait exactement à mes besoins, pour gérer mon site et le service clientèle de mes autres logiciels. Aucun client mail par ailleurs, à part Gaston, n’est purement français (écrit par un français). Enfin, je voulais faire une application en relation avec Internet.

**Quelles sont d’après vous les fonctions indispensables d’un logiciel de messagerie ?**
Sans hésiter, la notification des messages qui permet d’être tout le temps au courant de l’arrivée de nouveaux messages. L’anti-spam est aussi indispensable, vue la place qu’occupent les spams dans nos boîtes aux lettres. Et une interface costaud, qui permet de retrouver ses mails en deux trois clics.

**En pratique, en quoi consiste le développement d’un logiciel de messagerie ?**
Tout d’abord à essayer de trouver ce qui manque aux autres logiciels, donc faire preuve d’imagination. Ca ne sert à rien de faire une copie d’un logiciel existant. Ensuite connaître un langage de programmation sur le bout des doigts, c’est même plus qu’indispensable. Puis se plonger dans les RFC, qui décrivent tous les protocoles de communication comme IMAP, SSL, POP3, SMTP, TLS. Ensuite vient la phase développement, il faut beaucoup de temps et du coca lool ;). Enfin une fois le logiciel sorti, il faut le maintenir à jour (corriger les bugs, ajouter des fonctions, répondre aux utilisateurs)

**Qu’est-ce qui a pris le plus de temps ? Qu’est-ce qui a été le plus difficile ?**
Ce qui a pris le plus de temps à faire dans la conception du logiciel est sans hésiter la correction de bugs : ça fait pratiquement depuis juin 2004, que je fais ça. Pour le plus dur, la sécurisation SLL/TLS et tout ce qui est cryptage.

**Avez-vous dû faire des investissements ?**
Oui du temps (plus de 10 mois) et financièrement Delphi qui vaut 750 €.

**Pourquoi avoir choisi le modèle freeware ?**
Au début, Client Mail Checker était un shareware, il me rapportait plus d’argent mais ce n’est pas ça réellement qui m’intéresse. A l’heure actuelle, c’est surtout de me faire connaître pour pouvoir trouver une place dans une bonne école et peut-être un job par la suite.

**Quelles sont les prochaines évolutions prévues pour le logiciel ?**
Un Popper [utilitaire permettant de relever les messages, NDLR] pour les adresses Hotmail et MSN. Le logiciel sera aussi freeware, et Client Mail Checker deviendra une suite de logiciels dédiée à la messagerie. Une version anglaise est également prévue. C’est un ami qui s’en occupe.

**Maintenant que vous avez-mis les mains sous le capot, quel avis portez-vous sur les principaux logiciels de messagerie ?**
C’est l’heure des comptes loool. J’ai eu l’occasion de tester plein de logiciels pour voir si tout était compatible, Outlook Express est le grand vainqueur, il respecte tout, très simple d’utilisation, mais très peu d’options. Eudora : excellent logiciel, rien à redire, beaucoup d’options, mais je n’aime pas l’ergonomie, chacun ses goûts. Thunderbird et Pegasus Mail sont très bon aussi ! IncrediMail est une horreur à rendre compatible, j’en ai perdu des cheveux. Sans compter les bugs de ce logiciel, très joli, mais très mal programmé. S’il y a des RFC et des normes, c’est pour les respecter.Propos recueillis le 3 novembre 2004.

Propos recueillis par [Arobase.org](https://www.arobase.org/softs/cmc-itw.htm)
````
