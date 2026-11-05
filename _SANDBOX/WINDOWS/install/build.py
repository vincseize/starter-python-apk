from __future__ import annotations

import os
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
PYTHON = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
FLUTTER_BIN = Path(r"C:\flutter\3.44.8\bin")
ANDROID_SDK = Path(r"C:\AndroidSdk")
PUB_CACHE = Path(r"C:\pub-cache")

def main() -> int:
    if not PYTHON.is_file():
        print("Environnement non installé. Lancez d'abord install.bat.")
        return 1
    if not (PROJECT_ROOT / "src" / "main.py").is_file():
        print("ERREUR : src\\main.py introuvable.")
        return 1

    env = os.environ.copy()
    if FLUTTER_BIN.is_dir():
        env["PATH"] = str(FLUTTER_BIN) + os.pathsep + env.get("PATH", "")
    if ANDROID_SDK.is_dir():
        env["ANDROID_HOME"] = str(ANDROID_SDK)
        env["ANDROID_SDK_ROOT"] = str(ANDROID_SDK)
    if PUB_CACHE.is_dir():
        env["PUB_CACHE"] = str(PUB_CACHE)

    print("=" * 64)
    print(" COMPILATION DE L'APK ANDROID")
    print("=" * 64)
    command = [str(PYTHON), "-m", "flet", "build", "apk", "src"]
    result = subprocess.call(command, cwd=PROJECT_ROOT, env=env)

    if result == 0:
        print("\nCompilation terminée.")
        print(f"Vérifiez les APK dans : {PROJECT_ROOT / 'build' / 'apk'}")
        print("Selon la version de Flet, un autre dossier de sortie peut être utilisé.")
    else:
        print(f"\nÉchec de la compilation (code {result}).")
    return result

if __name__ == "__main__":
    raise SystemExit(main())
