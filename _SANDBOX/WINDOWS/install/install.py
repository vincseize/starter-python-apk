from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
VENV_DIR = PROJECT_ROOT / ".venv"
REQUIREMENTS = PROJECT_ROOT / "requirements.txt"

def run(command: list[str], *, env=None) -> None:
    print("\n> " + subprocess.list2cmdline(command), flush=True)
    subprocess.run(command, cwd=PROJECT_ROOT, env=env, check=True)

def main() -> int:
    print("=" * 64)
    print(" STARTER PYTHON APK - INSTALLATION DE L'ENVIRONNEMENT")
    print("=" * 64)
    print(f"Projet : {PROJECT_ROOT}")

    if not (PROJECT_ROOT / "src" / "main.py").is_file():
        print("\nERREUR : src\\main.py est introuvable.")
        print("Placez ce dossier dans : _SANDBOX\\WINDOWS\\install")
        return 1

    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    else:
        print("\n[OK] Environnement virtuel déjà présent.")

    python = VENV_DIR / "Scripts" / "python.exe"
    pip = [str(python), "-m", "pip"]

    run(pip + ["install", "--upgrade", "pip"])

    if REQUIREMENTS.is_file():
        run(pip + ["install", "-r", str(REQUIREMENTS)])
    else:
        print("\n[INFO] requirements.txt absent : installation de Flet.")
        run(pip + ["install", "flet"])

    # Flet is required for the run/build commands.
    run(pip + ["install", "flet"])

    flutter_bin = Path(r"C:\flutter\3.44.8\bin")
    android_sdk = Path(r"C:\AndroidSdk")
    env = os.environ.copy()

    if flutter_bin.is_dir():
        env["PATH"] = str(flutter_bin) + os.pathsep + env.get("PATH", "")
        print(f"\n[OK] Flutter détecté : {flutter_bin}")
    else:
        print(f"\n[AVERTISSEMENT] Flutter non trouvé dans : {flutter_bin}")
        print("Adaptez le chemin dans les scripts si nécessaire.")

    if android_sdk.is_dir():
        env["ANDROID_HOME"] = str(android_sdk)
        env["ANDROID_SDK_ROOT"] = str(android_sdk)
        print(f"[OK] Android SDK détecté : {android_sdk}")
    else:
        print(f"\n[AVERTISSEMENT] Android SDK non trouvé dans : {android_sdk}")

    print("\n" + "=" * 64)
    print(" INSTALLATION TERMINEE")
    print("=" * 64)
    print("Vous pouvez maintenant lancer : run_app.bat ou build_apk.bat")
    print("Si Flutter/Android SDK vient d'être installé, vérifiez aussi :")
    print("  flutter doctor")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"\nERREUR : une commande s'est terminée avec le code {exc.returncode}.")
        raise SystemExit(exc.returncode)
