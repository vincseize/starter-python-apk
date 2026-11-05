STARTER PYTHON APK - OUTILS WINDOWS
===================================

EMPLACEMENT
-----------
Copiez le dossier "install" dans :
C:\xampp\htdocs\starter-python-apk\_SANDBOX\WINDOWS\install

L'arborescence attendue :
starter-python-apk\
  src\
    main.py
  requirements.txt
  _SANDBOX\
    WINDOWS\
      install\
        install.py / install.bat
        run.py / run_app.bat
        build.py / build_apk.bat

UTILISATION
-----------
1. Double-cliquez sur install.bat
   - crée .venv à la racine du projet ;
   - met pip à jour ;
   - installe requirements.txt si présent ;
   - s'assure que Flet est installé.

2. Double-cliquez sur run_app.bat
   - lance l'application avec Flet : flet run src.

3. Double-cliquez sur build_apk.bat
   - lance la compilation : flet build apk src.

CONFIGURATION
-------------
Les scripts utilisent les chemins suivants, correspondant à votre configuration :
  Flutter : C:\flutter\3.44.8\bin
  Android SDK : C:\AndroidSdk
  Cache Pub : C:\pub-cache

Si vos chemins diffèrent, modifiez les constantes au début de install.py,
run.py et build.py.

PRÉREQUIS
---------
- Python installé et accessible via "py" ou "python".
- Flutter SDK installé.
- Android SDK et outils de compilation Android installés.
- Licences Android acceptées (flutter doctor --android-licenses).

NOTES
-----
- Les scripts ne téléchargent ni n'installent automatiquement Flutter ou Android SDK.
- Le dossier de sortie APK est généralement build\apk ; vérifiez aussi les
  messages de Flet en cas de changement de version.
- Le projet doit contenir src\main.py.
