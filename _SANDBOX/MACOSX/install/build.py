from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
PYTHON = PROJECT_ROOT / ".venv" / "bin" / "python"

def main() -> int:
    if not PYTHON.is_file():
        print("Environnement non installé. Lancez install.command.")
        return 1
    if not (PROJECT_ROOT / "src" / "main.py").is_file():
        print("ERREUR : src/main.py introuvable.")
        return 1

    env = os.environ.copy()
    print("=" * 64)
    print(" COMPILATION DE L'APPLICATION")
    print("=" * 64)

    command = [str(PYTHON), "-m", "flet", "build", "apk", "src"]
    result = subprocess.call(command, cwd=PROJECT_ROOT, env=env)

    if result == 0:
        print("\nCompilation terminée.")
        print(f"Vérifiez les APK dans : {PROJECT_ROOT / 'build' / 'apk'}")
        print("Selon la version de Flet, le dossier de sortie peut varier.")
    else:
        print(f"\nÉchec de la compilation (code {result}).")
    return result

if __name__ == "__main__":
    raise SystemExit(main())
