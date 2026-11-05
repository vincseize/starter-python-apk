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
    print("Démarrage de l'application Flet...")
    return subprocess.call(
        [str(PYTHON), "-m", "flet", "run", "src"],
        cwd=PROJECT_ROOT,
        env=env,
    )

if __name__ == "__main__":
    raise SystemExit(main())
