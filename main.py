import flet as ft
from flet import * 
from bg import BackgroundContainer

def main(page:Page):
    page.title='Youtube Downloader'
    page.window.width=500
    page.window.height=650

    background= BackgroundContainer().get_container()
    page.add(background)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

