import flet as ft
from flet import *

class BackgroundContainer():
    def __init__(self):

        self.background_container = ft.Container(
            
            content=ft.Column(
                controls=[
                    ft.Text(" YuTubbyX", size=60, font_family='VT323', text_align='center'),
                    ft.Text("A Youtube Downloader", size=30, font_family='VT323')
                ],
                spacing=0
                
            ),

            gradient=ft.LinearGradient(
                colors=["#FF0000", "#0000FF"],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right
            ),
            
            alignment=ft.alignment.center,
            margin=margin.all(-10),
            expand=True,
            padding=0
        )

    def get_container(self):
        return self.background_container