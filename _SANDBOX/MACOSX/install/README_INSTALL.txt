STARTER PYTHON APK - OUTILS macOS
=================================

EMPLACEMENT
-----------
Copiez le dossier "install" dans :
starter-python-apk/_SANDBOX/MACOS/install

Arborescence attendue :
starter-python-apk/
  src/
    main.py
  requirements.txt
  _SANDBOX/
    MACOS/
      install/
        install.py
        install.command
        run.py
        run_app.command
        build.py
        build_apk.command

UTILISATION
-----------
1. Ouvrez Terminal et rendez les scripts exécutables :
   chmod +x install.command run_app.command build_apk.command

2. Lancez ./install.command
   - crée .venv à la racine du projet ;
   - met pip à jour ;
   - installe requirements.txt si présent ;
   - s'assure que Flet est installé.

3. Lancez ./run_app.command pour démarrer l'application.

4. Lancez ./build_apk.command pour générer l'APK Android.

PRÉREQUIS
---------
- macOS.
- Python 3 accessible via python3.
- Flutter SDK installé et accessible dans le PATH.
- Android SDK installé et configuré.
- Licences Android acceptées :
  flutter doctor --android-licenses

ANDROID
-------
La compilation APK nécessite Android SDK et les outils Android configurés.
Vérifiez l'environnement avec :
  flutter doctor

NOTES
-----
- Ces scripts ne téléchargent pas automatiquement Flutter ni Android SDK.
- La compilation Android sur macOS nécessite la configuration Android.
- Le dossier APK est généralement build/apk ; vérifiez les messages de Flet.
- Le projet doit contenir src/main.py.
- Les scripts créent l'environnement virtuel .venv à la racine du projet.
