import flet as ft
from flet import *

class BackgroundContainer():
    def __init__(self):

        self.background_container = ft.Container(
            
            content=ft.Column(
                controls=[
                    ft.Text("Youtube Downloader", size=24)
                ]
                
            ),

            gradient=ft.LinearGradient(
                colors=["#FF0000", "#0000FF"],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right
            ),
            
            alignment=ft.alignment.center,
            margin=margin.all(-10),
            expand=True,
            padding=0,
        )

    def get_container(self):
        return self.background_container