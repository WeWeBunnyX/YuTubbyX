from turtle import bgcolor
import flet as ft
from flet import *

class Elements():
    def __init__(self):

        self.input_container = Container(

            content=Stack(
                controls=[
                    ft.TextField(hint_text="Enter the video link", width=700, height=50)

                ],

                alignment=ft.alignment.center
          
                



               


            ),
            alignment=ft.Alignment(0,-0.6),
            
            



        )

    def get_container(self):
        return self.input_container

