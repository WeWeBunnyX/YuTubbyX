import flet as ft
from flet import *

class Elements():
    def __init__(self):

        self.input_container = Container(

            content=Row(
                controls=[
                    ft.TextField(hint_text="Enter the video link")   

                ],

               



            ),

            expand=True,
            alignment=ft.alignment.top_left

            



        )

    def get_container(self):
        return self.input_container

