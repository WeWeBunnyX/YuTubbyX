import flet as ft
from flet import *
from pytube import YouTube



class Elements:
    def __init__(self):

        self.text_field = TextField(hint_text="Enter the video link", width=700, height=50)

        self.text_field_container = Container(
            content= self.text_field,
            alignment=ft.Alignment(0, 0.7),
            #bgcolor='blue',
            height=260
        )

        self.mp4_button = ElevatedButton("Convert to MP4", on_click= self.on_click_event)

        self.button_container = Container(
            content=self.mp4_button,
            alignment=ft.Alignment(0, -1),
            #bgcolor='purple',
            expand=True,
        )

        self.input_container = Container(
            content=Column(
                controls=[
                    self.text_field_container,
                    self.button_container
                ],
                alignment=MainAxisAlignment.CENTER,
                spacing=0
                
            ),
            expand=True,
            #bgcolor='white'
            
           
        )



    def on_click_event(self, e:ControlEvent):
        
        yt_url = self.text_field.value
        print(f"Video URL: {yt_url}")
        yt = YouTube(yt_url)

        video_title = yt.title
        print(f"Video Title: {video_title}")

        










    def get_containers(self):
        return self.input_container
