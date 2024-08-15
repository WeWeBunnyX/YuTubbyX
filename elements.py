import flet as ft
from flet import *
from pytubefix import YouTube
from pytubefix.exceptions import *
from moviepy.editor import *
import os


class Elements:
    def __init__(self, page:Page):
        self.page = page


        self.text_field = TextField(hint_text="Enter the video link", width=700, height=50)

        self.text_field_container = Container(
            content= self.text_field,
            alignment=ft.Alignment(0, 0.7),
            #bgcolor='blue',
            height=220
        )



        self.mp4_button = ElevatedButton("Convert to MP4", on_click= self.on_click_event)

        self.button_container = Container(
            content=self.mp4_button,
            alignment=ft.Alignment(0, -1),
            #bgcolor='purple',
            height = 50
        )



        self.image = Image(src="null", width=500, height=500)

        self.image_container = Container(
            content=self.image,
            alignment=ft.alignment.center,
            expand=True,
            #bgcolor='pink',
            
        )


        self.download360p_button = ElevatedButton("Download 360p", on_click=lambda e: self.download_video_quality('360p'))
        self.download480p_button = ElevatedButton("Download 480p",  on_click=lambda e: self.download_video_quality('480p'))
        self.download720p_button = ElevatedButton("Download 720p", on_click=lambda e: self.download_video_quality('720p'))
        self.download1080p_button = ElevatedButton("Download 1080p", on_click=lambda e: self.download_video_quality('1080p'))

        self.download_button_container = Container(
            content= Row(
                controls=[
                    self.download360p_button,
                    self.download480p_button,
                    self.download720p_button,
                    self.download1080p_button
                          
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
        


            ),
            #bgcolor='red',
            height=60,
            alignment=ft.alignment.center,
            visible=False
            

        )


        self.input_container = Container(
            content=Column(
                controls=[
                    self.text_field_container,
                    self.button_container,
                    self.image_container,
                    self.download_button_container
                    
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
         print()

         video_stream = yt.streams.filter( type='video', file_extension='mp4', progressive=False)
         print(f"{video_stream}")

         self.download_button_container.visible= True
         self.page.update()

         print()

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


    def download_video_quality(self, resolution:str):
        yt_url = self.text_field.value
        yt = YouTube(yt_url)

        video_stream = yt.streams.filter(res=resolution, only_video=True, progressive=False).first()
        self.download_audio()

        if video_stream is None:
         print(f"No stream found for resolution: {resolution}")

        if resolution == '360p':                 
         print("Downloading 360p video...")
         
        elif resolution == '480p':
         print("Downloading 480p video...")

        elif resolution == '720p':
         print("Downloading 720p video...")

        elif resolution == '1080p':
         print("Downloading 1080p video...")

        elif resolution == '1440p':
         print("Downloading 1440p video...")

        elif resolution == '2160p':
         print("Downloading 4K video (2160p)...")

        else:
         print("?")
    
        video_stream.download(output_path='C:/Users/SAMAMA/Desktop/App/Applicacion')
        self.audio_video_merge()
        


    def download_audio(self):
        yt_url = self.text_field.value
        yt = YouTube(yt_url)

        audio_stream = yt.streams.filter(adaptive=True, only_audio=True).last()
        print()
        print(f"{audio_stream}")

        audio_stream.download(output_path='C:/Users/SAMAMA/Desktop/App/Applicacion')


                
    def update_image_source(self, thumbnail_url: str):
         self.image.src = thumbnail_url
         self.image.update()


        
    def notif_snack_bar(self, message:str):
        snack_bar = SnackBar(
            content= Text(message),
            duration=1500, 
            action="Understood",
            open=True, 
        )

        self.page.snack_bar = snack_bar
        self.page.update()


    def get_containers(self):
        return self.input_container
    

    def audio_video_merge(self):
     yt_url = self.text_field.value
     yt = YouTube(yt_url)
     video_title = yt.title
    
     title = video_title.strip()  

     video_path = f"{title}.mp4"
     audio_path = f"{video_title}.webm"
     
     if not os.path.exists(video_path):
        print(f"Error: The video file {video_path} does not exist.")
        return
    
     if not os.path.exists(audio_path):
        print(f"Error: The audio file {audio_path} does not exist.")
        return

     try:
         video_clip = VideoFileClip(video_path)
         audio_clip = AudioFileClip(audio_path)

     except FileNotFoundError as e:
        print(f"Error: {e}")
        return

     final_clip = video_clip.set_audio(audio_clip)

     output_file = f"{title}_merged.mp4"
     final_clip.write_videofile(output_file, codec='libx264')

     video_clip.close()
     audio_clip.close()
     final_clip.close()

     print(f"Video saved as {output_file}")