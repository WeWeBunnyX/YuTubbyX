import flet as ft
from flet import *


class Elements:
    def __init__(self):
        self.text_field_container = Container(
            content=TextField(hint_text="Enter the video link", width=700, height=50),
            alignment=ft.Alignment(0, 0.6)
        )

        self.button_container = Container(
            content=ElevatedButton("Convert to MP4"),
            alignment=ft.Alignment(0, -1)
        )

        self.input_container = Container(
            content=Column(
                controls=[
                    self.text_field_container,
                    self.button_container
                ],
                alignment=MainAxisAlignment.CENTER  # Center the children vertically
            ),
            expand=True
        )

    def get_containers(self):
        return self.input_container
