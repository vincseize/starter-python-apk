from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
VENV_DIR = PROJECT_ROOT / ".venv"
REQUIREMENTS = PROJECT_ROOT / "requirements.txt"

def run(command: list[str], *, env=None) -> None:
    print("\n> " + " ".join(command), flush=True)
    subprocess.run(command, cwd=PROJECT_ROOT, env=env, check=True)

def main() -> int:
    print("=" * 64)
    print(" STARTER PYTHON APK - INSTALLATION macOS")
    print("=" * 64)
    print(f"Projet : {PROJECT_ROOT}")

    if not (PROJECT_ROOT / "src" / "main.py").is_file():
        print("\nERREUR : src/main.py est introuvable.")
        print("Placez ce dossier dans _SANDBOX/MACOS/install.")
        return 1

    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    else:
        print("\n[OK] Environnement virtuel déjà présent.")

    python = VENV_DIR / "bin" / "python"
    pip = [str(python), "-m", "pip"]
    run(pip + ["install", "--upgrade", "pip"])

    if REQUIREMENTS.is_file():
        run(pip + ["install", "-r", str(REQUIREMENTS)])
    else:
        print("\n[INFO] requirements.txt absent : installation de Flet.")
        run(pip + ["install", "flet"])

    run(pip + ["install", "flet"])

    env = os.environ.copy()
    flutter_candidates = [
        Path.home() / "development" / "flutter" / "bin",
        Path.home() / "flutter" / "bin",
        Path("/opt/homebrew/bin"),
    ]
    flutter_bin = next((p for p in flutter_candidates if (p / "flutter").exists()), None)

    if flutter_bin:
        env["PATH"] = str(flutter_bin) + os.pathsep + env.get("PATH", "")
        print(f"\n[OK] Flutter détecté : {flutter_bin}")
    elif shutil.which("flutter", path=env.get("PATH")):
        print(f"\n[OK] Flutter accessible : {shutil.which('flutter')}")
    else:
        print("\n[AVERTISSEMENT] Flutter n'est pas détecté dans le PATH.")
        print("Installez Flutter puis configurez son PATH avant de compiler.")

    if not env.get("ANDROID_HOME") and not env.get("ANDROID_SDK_ROOT"):
        print("[INFO] Android SDK : configurez ANDROID_HOME ou ANDROID_SDK_ROOT si nécessaire.")

    print("\n" + "=" * 64)
    print(" INSTALLATION TERMINEE")
    print("=" * 64)
    print("Lancez run_app.command pour démarrer ou build_apk.command pour compiler.")
    print("Vérifiez l'environnement Android avec : flutter doctor")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"\nERREUR : une commande s'est terminée avec le code {exc.returncode}.")
        raise SystemExit(exc.returncode)
