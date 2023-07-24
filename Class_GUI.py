import tkinter as tk
import os
from Class_Playlist import Playlist as pl
from Class_Playlist import client_id
from Class_Playlist import client_secret


root = tk.Tk()
root.geometry("400x400")
root.title("Spotify Youtube Downloader")
label = tk.Label(root, text="Spotify Youtube Downloader", font=("Arial", 18))
label.pack(padx=10, pady=10)


class GUI():
    def __init__(self, master):
        self.labels = ["Spotify Playlist URL", "File Path"]
        self.master = master

    def playlist_texbox(self):
        self.textbox_label1 = tk.Label(self.master, text=self.labels[0], font=("Arial", 10))
        self.textbox_label1.pack(padx=10, pady=5)
        self.textbox1 = tk.Text(self.master, height=1, font=("Arial", 16))
        self.textbox1.pack(padx=10, pady=5)

    def destination_textbox(self):
        self.textbox_label2 = tk.Label(self.master, text=self.labels[1], font=("Arial", 10))
        self.textbox_label2.pack(padx=10, pady=5)
        self.textbox2 = tk.Text(self.master, height=1, font=("Arial", 16))
        self.textbox2.pack(padx=10, pady=5)

    def download(self):
        playlist_url = self.textbox1.get("1.0", tk.END).strip()
        destination_path = self.textbox2.get("1.0", tk.END).strip()
        playlist_tracks = pl.get_playlist_tracks(playlist_url, client_id, client_secret)
        pl.download_mp3(playlist_tracks, destination_path)

    def button(self):
        self.download_button = tk.Button(root, text="Download", font=("Arial", 16), command=self.download)
        self.download_button.pack(padx=10, pady=10)

#C:\\Users\\krak3rs\\Desktop\\songs
#https://open.spotify.com/playlist/2yGGIqke175hWZCAc5TvMt?si=86089765739b472b


gui1 = GUI(root)
gui1.playlist_texbox()
gui1.destination_textbox()
gui1.button()
root.mainloop()