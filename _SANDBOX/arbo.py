#!/usr/bin/env python3

from pathlib import Path


# Dossiers ignorés complètement (nom exact, à n'importe quel niveau)
DOSSIERS_IGNORES = {
    # Environnements virtuels
    "venv", ".venv", "env", "ENV", ".env",
    # Caches Python
    "__pycache__", ".pytest_cache", ".ruff_cache",
    ".mypy_cache", ".tox", ".nox",
    # Build / packaging
    "build", "dist", ".eggs",
    # Flet / Flutter / Android
    ".dart_tool", ".gradle", ".pub-cache", ".pub",
    ".flutter-plugins", ".flutter-plugins-dependencies",
    # Git
    ".git",
    # IDE
    ".vscode", ".idea",
    # Sandbox perso
    "_SANDBOX",
}

# Fichiers ignorés (nom exact)
FICHIERS_IGNORES = {
    ".gitignore",  # optionnel, retirer si on veut le voir
}


def afficher_arborescence(dossier: Path, fichier_sortie: Path) -> None:
    lignes = [f"{dossier.name}/"]

    def parcourir(chemin: Path, prefixe: str = "") -> None:
        try:
            elements = sorted(
                chemin.iterdir(),
                key=lambda element: (element.is_file(), element.name.lower()),
            )
        except PermissionError:
            lignes.append(f"{prefixe}└── [Accès refusé]")
            return

        elements = [
            element
            for element in elements
            if element.name not in FICHIERS_IGNORES
            and element.name not in DOSSIERS_IGNORES
            and element.resolve() != fichier_sortie.resolve()
        ]

        for index, element in enumerate(elements):
            dernier = index == len(elements) - 1
            branche = "└── " if dernier else "├── "
            nouveau_prefixe = prefixe + ("    " if dernier else "│   ")

            if element.is_dir():
                lignes.append(f"{prefixe}{branche}{element.name}/")
                parcourir(element, nouveau_prefixe)
            else:
                lignes.append(f"{prefixe}{branche}{element.name}")

    parcourir(dossier)

    fichier_sortie.write_text("\n".join(lignes) + "\n", encoding="utf-8")


if __name__ == "__main__":
    dossier_script = Path(__file__).resolve().parent
    dossier_a_analyser = dossier_script.parent
    fichier_sortie = dossier_script / "arbo.txt"

    afficher_arborescence(dossier_a_analyser, fichier_sortie)
    print(f"Arborescence enregistrée dans : {fichier_sortie}")