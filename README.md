````markdown
# 🧠 Outil de Subnetting IPv4 en Python

Ce projet est un outil léger en Python permettant de manipuler des adresses IPv4 et de réaliser des opérations de **subnetting** sans utiliser le module `ipaddress` ni d'autres bibliothèques standard.

---

## 🚀 Fonctionnalités

- ✅ Conversion d'une adresse IPv4 décimale en binaire (`ipv4_dec`)  
- ✅ Conversion d'une adresse IPv4 binaire en décimale (`ipv4_bin`)  
- ✅ Calcul manuel de :
  - l'adresse réseau  
  - l'adresse de diffusion (broadcast)  
  - la première adresse utilisable  
  - la dernière adresse utilisable       
  - le nombre d’hôtes possibles

---

## 🛠️ Installation

Aucune bibliothèque externe n’est requise.  
Assurez-vous simplement d’avoir **Python 3** installé sur votre machine.

```bash
git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd sub
python main.py
````

---

## 💻 Utilisation

Lancez le script et entrez une adresse IPv4 suivie de son préfixe réseau :
Exemple :

```
Adresse IP : 192.168.1.1  
Préfixe réseau : 24
```

Le programme renverra :

* Adresse réseau : 192.168.1.0
* Adresse de diffusion : 192.168.1.255
* Première adresse utilisable : 192.168.1.1
* Dernière adresse utilisable : 192.168.1.254
* Nombre d’hôtes : 254

---

## ⚠️ Limitations

* Toutes les vérifications (validité d’adresse, formats, valeurs hors plage) ne sont **pas encore implémentées**
* Ce projet est conçu à but pédagogique pour mieux comprendre le fonctionnement du subnetting

---

## 📂 Structure du projet

```text
.
├── main.py              # Script principal
├── utils.py             # Fonctions de conversion et de calcul
└── README.md            # Ce fichier
```

---

## 👨‍💻 Auteur

**Abdoul Gafar AMADOU**
Étudiant en Réseaux et Systèmes, passionné par le développement d’outils réseau et l’ingénierie logicielle.

---

## 📜 Licence

Ce projet est sous licence MIT — vous êtes libre de l'utiliser, le modifier et le redistribuer avec attribution.

```
