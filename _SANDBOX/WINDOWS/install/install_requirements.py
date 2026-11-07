import os
import subprocess
import sys

def check_requirements():
    print("--- Vérification et installation des dépendances ---")
    
    # 1. Vérifier si requirements.txt existe
    req_file = "requirements.txt"
    if not os.path.exists(req_file):
        print(f"[ERREUR] Le fichier '{req_file}' est introuvable à la racine.")
        return False

    # 2. Installer / Mettre à jour pip et les paquets depuis requirements.txt
    print("[INFO] Installation des dépendances listées dans requirements.txt...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
        print("[SUCCÈS] Toutes les dépendances sont installées.")
    except subprocess.CalledProcessError as e:
        print(f"[ERREUR] Une erreur est survenue lors de l'installation : {e}")
        return False

    return True

def create_env_file():
    print("\n--- Vérification du fichier .env ---")
    env_file = ".env"
    env_example = ".env.example"

    if os.path.exists(env_file):
        print(f"[INFO] Le fichier '{env_file}' existe déjà.")
        return

    # Contenu par défaut pour ton fichier .env (à adapter selon tes besoins)
    default_content = """# Configuration de l'application
APP_NAME=ICEANOTES
APP_ENV=development
DEBUG=True

# Paramètres additionnels (ex: Flet / Base de données)
# FLET_PORT=8550
"""

    # Si un modèle .env.example existe, on peut s'en inspirer, sinon on crée le .env par défaut
    target_content = default_content
    if os.path.exists(env_example):
        with open(env_example, "r", encoding="utf-8") as f:
            target_content = f.read()
        print(f"[INFO] Utilisation de '{env_example}' pour générer le '{env_file}'.")

    try:
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(target_content)
        print(f"[SUCCÈS] Fichier '{env_file}' créé avec succès.")
    except Exception as e:
        print(f"[ERREUR] Impossible de créer le fichier .env : {e}")

if __name__ == "__main__":
    success = check_requirements()
    if success:
        create_env_file()
        print("\n--- Configuration terminée avec succès ! ---")
    else:
        print("\n--- L'installation a échoué. ---")
        sys.exit(1)