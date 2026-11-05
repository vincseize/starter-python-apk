from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
PYTHON = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
FLUTTER_BIN = Path(r"C:\flutter\3.44.8\bin")
ANDROID_SDK = Path(r"C:\AndroidSdk")

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

    print("Démarrage de l'application Flet...")
    return subprocess.call(
        [str(PYTHON), "-m", "flet", "run", "src"],
        cwd=PROJECT_ROOT,
        env=env,
    )

if __name__ == "__main__":
    raise SystemExit(main())
