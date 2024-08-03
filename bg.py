import flet as ft
from flet import *

class BackgroundContainer():
    def __init__(self):

        self.background_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Youtube Downloader", size=24)
                ],
                
            ),
            padding=0,

            gradient=ft.LinearGradient(
                colors=["#FF0000", "#0000FF"],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right
            ),
            
            alignment=ft.alignment.center,
            width=500,
            height=650,
            margin=margin.all(-10)
        )

    def get_container(self):
        return self.background_container