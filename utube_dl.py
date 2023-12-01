import tkinter
import customtkinter
from pytube import YouTube
import os
import datetime


def startDownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        download_path = os.getcwd()  # Get the current working directory
        video_file_name = ytobject.title + ".mp4"  # Assuming the downloaded video has an mp4 extension
        video_file_path = os.path.join(download_path, video_file_name)
        finishlabel.configure(text="Downloaded. Video saved at: " + video_file_path)

        # Create a clickable link to open the video location
        link_label.configure(text=video_file_path)
        link_label.bind("<Button-1>", lambda e: os.startfile(video_file_path))
    except:
        finishlabel.configure(text="Youtube link is invalid")

# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)

# Video link
link_label = customtkinter.CTkLabel(app, text="")
link_label.pack(padx=10, pady=10)

# Run app
app.mainloop()
