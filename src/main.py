"""Starter Flet : fenêtre Hello World + bouton + splash screen.

Compatible Flet 1.0+ (utilise ft.run, ft.Button, ft.Icon(icon=...)).
"""

import asyncio

import flet as ft


# ---------------------------------------------------------------------------
# Splash screen
# ---------------------------------------------------------------------------
async def afficher_splash(page: ft.Page, duree: float = 2.0) -> None:
    """Affiche un splash screen pendant `duree` secondes."""
    splash = ft.Container(
        content=ft.Column(
            controls=[
                ft.ProgressRing(width=48, height=48, stroke_width=4),
                ft.Container(height=16),
                ft.Text("Chargement…", size=16, italic=True),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment.CENTER,
        expand=True,
    )

    page.controls.clear()
    page.add(splash)
    page.update()

    await asyncio.sleep(duree)


# ---------------------------------------------------------------------------
# Écran principal
# ---------------------------------------------------------------------------
def construire_ecran_principal(page: ft.Page) -> ft.Control:
    """Construit l'écran principal avec un titre et un bouton."""

    message = ft.Text(
        "Hello, World!",
        size=32,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    compteur = ft.Text(
        "Clics : 0",
        size=14,
        italic=True,
        color=ft.Colors.GREY,
    )

    etat = {"clics": 0}

    def on_clic(_: ft.ControlEvent) -> None:
        etat["clics"] += 1
        compteur.value = f"Clics : {etat['clics']}"
        message.value = f"Hello, World! ({etat['clics']})"
        page.update()

    bouton = ft.Button(
        content=ft.Row(
            controls=[
                ft.Icon(icon=ft.Icons.TOUCH_APP),
                ft.Text("Clique-moi"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            tight=True,
        ),
        on_click=on_clic,
    )

    return ft.Container(
        content=ft.Column(
            controls=[message, bouton, compteur],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.Alignment.CENTER,
        expand=True,
        padding=40,
    )


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------
async def main(page: ft.Page) -> None:
    page.title = "Starter Flet"
    page.window.width = 480
    page.window.height = 640
    page.window.min_width = 360
    page.window.min_height = 480
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.padding = 0

    # Phase 1 : splash
    await afficher_splash(page, duree=2.0)

    # Phase 2 : écran principal
    page.controls.clear()
    page.add(construire_ecran_principal(page))
    page.update()


if __name__ == "__main__":
    ft.run(main)