import flet as ft
from flet import * 
from bg import BackgroundContainer
from elements import Elements

def main(page:Page):
    page.title='Youtube Downloader'
    page.window.width=500
    page.window.height=650

    page.fonts = {
        "VT323": "fonts/VT323.ttf",
    }

    background= BackgroundContainer().get_container()
    ui_elements = Elements().get_container()

    main_container = ft.Container(
        content=ft.Stack(
            controls=[
                background,
                ui_elements,
            ],
        ),
        expand=True
    )
    

    page.add(main_container)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets')

