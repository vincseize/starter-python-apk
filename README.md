# 🚀 Starter Python APK

**Développer, exécuter et compiler des applications Android avec Python, Flet et Flutter.**

Starter Python APK est un environnement de développement permettant de créer des applications Android à partir de Python et du framework Flet.

Le projet fournit une base fonctionnelle comprenant une interface graphique, un écran de démarrage (*Splash Screen*) et des éléments interactifs.

Il intègre également des scripts permettant de simplifier l'installation de l'environnement, le lancement de l'application et la génération des fichiers APK.

---

## 📋 Sommaire

- [Technologies](#-technologies)
- [Structure du projet](#-structure-du-projet)
- [Prérequis](#-prérequis)
- [Installation automatique](#-installation-automatique)
- [Installation manuelle](#-installation-manuelle)
- [Configuration de Flutter](#-configuration-de-flutter)
- [Configuration Android](#-configuration-android)
- [Lancement de l'application](#-lancement-de-lapplication)
- [Compilation APK](#-compilation-apk)
- [Installation sur Android](#-installation-sur-android)
- [Dépannage](#-dépannage)
- [Commandes utiles](#-commandes-utiles)

---

## 🛠️ Technologies

| Technologie | Fonction |
|---|---|
| Python | Langage de programmation |
| Flet | Interface graphique |
| Flutter SDK | Environnement de compilation |
| Dart | Technologie utilisée par Flutter |
| Android SDK | Compilation Android |
| ADB | Communication avec les appareils Android |
| Visual Studio Code | Éditeur de code |

---

## 📁 Structure du projet

```text
starter-python-apk/
│
├── src/
│   ├── .flet/
│   │   └── storage/
│   ├── assets/
│   │   └── splash.png
│   ├── __init__.py
│   └── main.py
│
├── _SANDBOX/
│   └── WINDOWS/
│       └── install/
│           ├── install.py
│           ├── install.bat
│           ├── run.py
│           ├── run_app.bat
│           ├── build.py
│           └── build_apk.bat
│
├── _SANDBOX/
│   └── MACOS/
│       └── install/
│           ├── install.py
│           ├── install.command
│           ├── run.py
│           ├── run_app.command
│           ├── build.py
│           └── build_apk.command
│
├── .venv/
├── requirements.txt
└── README.md
```

---

## 💻 Prérequis

### Environnement Windows

- Windows 10 ou Windows 11
- Python 3
- Flutter SDK
- Android SDK
- Visual Studio Code (recommandé)

### Environnement macOS

- macOS
- Python 3
- Flutter SDK
- Android SDK
- Xcode et ses outils en ligne de commande (recommandés pour l'environnement Apple)

### Versions de référence

| Composant | Version |
|---|---|
| Flutter | 3.44.8 |
| Dart | 3.12.2 |
| Canal Flutter | Stable |
| Framework | Flet |
| Plateforme cible | Android |

---

## ⚡ Installation automatique

Le projet intègre des scripts pour automatiser les principales opérations.

Chaque système dispose de son propre dossier d'installation.

### 🪟 Windows

Emplacement :

```text
_SANDBOX/WINDOWS/install/
```

| Fichier | Fonction |
|---|---|
| `install.bat` | Installation de l'environnement |
| `install.py` | Script d'installation Python |
| `run_app.bat` | Lancement de l'application |
| `run.py` | Exécution de l'application |
| `build_apk.bat` | Compilation Android |
| `build.py` | Script de compilation |

**Installation :**

Double-cliquez sur :

```text
install.bat
```

**Lancer l'application :**

```text
run_app.bat
```

**Compiler l'APK :**

```text
build_apk.bat
```

### 🍎 macOS

Emplacement :

```text
_SANDBOX/MACOS/install/
```

| Fichier | Fonction |
|---|---|
| `install.command` | Installation de l'environnement |
| `install.py` | Script d'installation Python |
| `run_app.command` | Lancement de l'application |
| `run.py` | Exécution de l'application |
| `build_apk.command` | Compilation Android |
| `build.py` | Script de compilation |

**Première utilisation :**

Ouvrez le Terminal à la racine du projet et exécutez :

```bash
cd _SANDBOX/MACOS/install

chmod +x *.command
```

**Installation :**

```bash
./install.command
```

**Lancer l'application :**

```bash
./run_app.command
```

**Compiler l'APK :**

```bash
./build_apk.command
```

---

## ⚙️ Installation manuelle

Si vous préférez configurer votre environnement manuellement, suivez les étapes ci-dessous.

### 1. Installer Python

Téléchargement :

https://www.python.org/downloads/

Vérification :

```bash
python --version
```

Sur macOS :

```bash
python3 --version
```

### 2. Créer l'environnement virtuel

À la racine du projet :

**Windows :**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS :**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Sur macOS, utilisez `python3` pour les commandes exécutées hors environnement virtuel.

---

## 🐦 Configuration de Flutter

### 1. Installer Flutter SDK

Documentation officielle :

https://docs.flutter.dev/get-started/install

Version de référence du projet : **Flutter 3.44.8**.

### 2. Configurer le PATH

Le dossier `bin` de Flutter doit être accessible depuis le terminal.

Exemple Windows :

```text
C:\flutter\3.44.8\bin
```

Exemple macOS :

```text
~/development/flutter/bin
```

### 3. Vérifier l'installation

```bash
flutter --version
flutter doctor
```

Flutter doit être correctement détecté avant de lancer une compilation.

---

## 🤖 Configuration Android

### 1. Installer Android SDK

Installez Android Studio :

https://developer.android.com/studio

Utilisez le gestionnaire SDK pour installer les composants nécessaires :

- Android SDK Platform
- Android SDK Build-Tools
- Android SDK Command-line Tools
- Android SDK Platform-Tools

### 2. Configurer le SDK

Exemple Windows :

```powershell
flutter config --android-sdk C:\AndroidSdk
```

Sur macOS, définissez le chemin correspondant à votre installation :

```bash
export ANDROID_HOME="$HOME/Library/Android/sdk"
export ANDROID_SDK_ROOT="$ANDROID_HOME"
```

### 3. Accepter les licences

```bash
flutter doctor --android-licenses
```

### 4. Vérifier la configuration

```bash
flutter doctor
```

---

## ▶️ Lancement de l'application

### Avec Flet

```bash
flet run src
```

### Avec Python

**Windows :**

```powershell
.venv\Scripts\activate
python src\main.py
```

**macOS :**

```bash
source .venv/bin/activate
python src/main.py
```

---

## 🏗️ Compilation APK

La compilation permet de transformer le projet Python en application Android installable.

### 1. Préparer l'environnement

Vérifiez que Python, Flet, Flutter et Android SDK sont correctement configurés.

### 2. Nettoyer les anciens fichiers

**Windows :**

```powershell
Remove-Item -Recurse -Force src\build -ErrorAction SilentlyContinue
```

**macOS :**

```bash
rm -rf src/build
```

### 3. Générer l'APK

Depuis la racine du projet :

```bash
flet build apk src
```

### 4. Vérifier les fichiers générés

Le dossier de sortie utilisé par le projet est généralement :

```text
build/apk/
```

Selon la version de Flet et la configuration du projet, les fichiers peuvent également être présents dans les sous-dossiers de compilation de `src/build/`.

---

## 📱 Installation sur Android

### Méthode 1 — Installation USB avec ADB

1. Activez les options développeur sur votre téléphone.
2. Activez le débogage USB.
3. Connectez votre appareil à l'ordinateur.
4. Vérifiez la détection de l'appareil :

```bash
adb devices
```

5. Installez l'application :

```bash
adb install -r build/apk/app-release.apk
```

### Méthode 2 — Installation manuelle

1. Transférez le fichier APK sur votre téléphone.
2. Ouvrez le fichier.
3. Autorisez l'installation si nécessaire.
4. Installez et démarrez l'application.

---

## 🔧 Dépannage

### Flutter n'est pas reconnu

Vérifiez que le dossier `bin` de Flutter est présent dans le PATH.

```bash
flutter --version
```

### Android SDK non détecté

```bash
flutter doctor
```

Vérifiez également les variables `ANDROID_HOME` et `ANDROID_SDK_ROOT`.

### Problème de dépendances Python

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Problème de compilation

Nettoyez les anciens fichiers :

```bash
flet build apk src
```

Si nécessaire, supprimez les anciens dossiers de compilation avant de recommencer.

### Vérification générale

```bash
flutter doctor -v
```

---

## ⌨️ Commandes utiles

| Commande | Description |
|---|---|
| `python --version` | Version Python |
| `pip list` | Dépendances installées |
| `flutter --version` | Version Flutter |
| `flutter doctor` | Diagnostic Flutter |
| `flet run src` | Lancement de l'application |
| `flet build apk src` | Compilation APK |
| `adb devices` | Appareils Android connectés |
| `adb install -r app-release.apk` | Installation APK |
| `deactivate` | Quitter l'environnement virtuel |

---

## ✅ État du projet

**Compilation Android validée.**

Une génération APK a été effectuée avec succès sur l'environnement Windows.

Résultat obtenu :

```text
Packaged Python app
Built .apk for Android
Copied build to build\apk directory

Successfully built your .apk for Android!
```

---

## 📌 Informations

| Propriété | Valeur |
|---|---|
| Projet | Starter Python APK |
| Langage | Python |
| Interface | Flet |
| Compilation | Flutter |
| Cible | Android |
| Environnements | Windows / macOS |
| Format de sortie | APK |

---

**Starter Python APK**

*Un environnement simple, structuré et évolutif pour développer et déployer des applications Android avec Python.* 🚀