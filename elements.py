import flet as ft
from flet import *
from pytube import YouTube
from pytube.exceptions import *



class Elements:
    def __init__(self, page:Page):
        self.page = page

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
            height = 100
        )


        self.image = Image(src="null", width=500, height=500)

        self.image_container = Container(
            content=self.image,
            alignment=ft.alignment.center,
            expand=True,
            #bgcolor='pink'
        )


        self.input_container = Container(
            content=Column(
                controls=[
                    self.text_field_container,
                    self.button_container,
                    self.image_container
                    
                ],
                alignment=MainAxisAlignment.CENTER,
                spacing=0
                
            ),
            expand=True,
            #bgcolor='white'
        )




    def on_click_event(self, e:ControlEvent):
        
        try:
         yt_url = self.text_field.value
         print(f"Video URL: {yt_url}")
         yt = YouTube(yt_url)

         video_title = yt.title
         print(f"Video Title: {video_title}")

         video_thumbnail = yt.thumbnail_url
         print(f"Thumbnail URL: {video_thumbnail}")
         self.update_image_source(video_thumbnail)

        except LiveStreamError:
            print("The video is a live stream, which cannot be processed.")
        except RegexMatchError:
            print("The provided URL is not a valid YouTube URL.")
            self.notif_snack_bar("The provided URL is not a valid YouTube URL")
        except MembersOnly:
            print("Members only")    
        except VideoUnavailable:
            print("The video is unavailable. It may have been removed or restricted.")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
            


    def update_image_source(self, thumbnail_url: str):
         self.image.src = thumbnail_url
         self.image.update()


        
    def notif_snack_bar(self, message:str):
        snack_bar = SnackBar(
            content= Text(message),
            duration=8, 
            open=True, 
        )

        self.page.snack_bar = snack_bar
        self.page.update()


    def get_containers(self):
        return self.input_container
