# 🚀 Starter Python APK

**Projet de démarrage pour développer une application Android avec Python et Flet.**

Ce projet fournit une base simple et évolutive pour créer une application avec une interface graphique moderne, intégrant une fenêtre d'accueil, un bouton interactif et un écran de démarrage (*Splash Screen*).

L'objectif est de disposer d'un environnement de développement prêt à être personnalisé et à évoluer vers la génération d'un fichier APK Android.

---

## 📌 Technologies utilisées

- **Python** : langage principal du projet.
- **Flet** : création d'interfaces graphiques avec Python.
- **Flutter SDK** : environnement nécessaire aux outils de développement et de compilation associés.
- **Briefcase** : outil de packaging d'applications Python.
- **Toga** : framework d'interfaces graphiques multiplateformes.
- **Visual Studio Code** : environnement de développement recommandé.

---

## 📁 Structure du projet

```text
starter-python-apk/
│
├── .venv/                 # Environnement virtuel Python
├── main.py                # Point d'entrée de l'application
├── requirements.txt       # Dépendances Python
├── README.md              # Documentation du projet
└── assets/                # Ressources graphiques
```

*Cette structure est indicative et peut être adaptée selon l'évolution du projet.*

---

## ⚙️ Installation et configuration

### 1. Installer Python

Téléchargez et installez Python sur votre ordinateur.

Vérifiez son installation :

```bash
python --version
```

### 2. Installer Visual Studio Code

Installez [Visual Studio Code](https://code.visualstudio.com/).

Ajoutez les extensions nécessaires au développement Python et Flutter.

### 3. Installer Flutter SDK

Dans Visual Studio Code :

1. Ouvrez la palette de commandes avec `Ctrl + Shift + P`.
2. Recherchez `Flutter`.
3. Sélectionnez **Flutter: Install Flutter SDK**.
4. Suivez les instructions d'installation.

Visual Studio Code peut ajouter automatiquement Flutter au PATH selon la configuration de votre environnement.

Vérifiez ensuite l'installation :

```bash
flutter doctor
```

### 4. Créer l'environnement virtuel

À la racine du projet, exécutez :

```bash
python -m venv .venv
```

Activez l'environnement virtuel sous Windows :

```powershell
.venv\Scripts\activate
```

### 5. Installer les dépendances

Installez Flet :

```bash
pip install flet
```

Installez également Flet Desktop :

```bash
pip install flet-desktop==1.0.5
```

Installez Briefcase :

```bash
python -m pip install briefcase
```

Installez Toga :

```bash
python -m pip install --pre toga
```

Si le fichier `requirements.txt` est disponible et correctement renseigné, vous pouvez également installer les dépendances avec :

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l'application

Une fois les dépendances installées et l'environnement virtuel activé, lancez l'application :

```bash
python main.py
```

L'application démarre avec :

- Une fenêtre d'accueil « Hello World ».
- Un bouton interactif.
- Un écran de démarrage (*Splash Screen*).
- Une base de code prête à être personnalisée.

---

## 📱 Objectif Android APK

Le projet a vocation à évoluer vers une application Android installable.

Les prochaines étapes de développement pourront inclure :

- La personnalisation de l'interface graphique.
- L'intégration d'un logo et d'une icône d'application.
- L'ajout de nouvelles fonctionnalités.
- La configuration de l'environnement Android.
- La préparation et la génération du fichier APK.

---

## 🛠️ Commandes utiles

| Commande | Description |
|---|---|
| `python --version` | Vérifier Python |
| `flutter doctor` | Vérifier Flutter |
| `pip install flet` | Installer Flet |
| `pip list` | Afficher les dépendances |
| `python main.py` | Lancer l'application |
| `deactivate` | Quitter l'environnement virtuel |

---

## 👨‍💻 Développement

Pour commencer à travailler sur le projet :

1. Ouvrez le dossier dans Visual Studio Code.
2. Activez l'environnement virtuel.
3. Installez les dépendances.
4. Modifiez le fichier `main.py`.
5. Lancez l'application pour tester vos modifications.

---

## 📄 Licence

Projet de démarrage destiné à l'apprentissage, au développement et à la personnalisation d'applications Python.

---

**Starter Python APK — Une base simple pour construire votre future application Android.** 🚀

Flutter SDK 3.44.8 is required.

Android SDK is required.