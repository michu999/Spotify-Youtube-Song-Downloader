import tkinter as tk
from playlist import Playlist, client_id, client_secret


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Spotify YouTube Downloader")
        self.master.geometry("400x400")

        self.labels = ["Spotify Playlist URL", "File Path"]
        self.create_widgets()

    def create_widgets(self):
        """Creates the GUI components."""
        tk.Label(self.master, text="Spotify YouTube Downloader", font=("Arial", 18)).pack(padx=10, pady=10)

        self.create_textbox(self.labels[0], 1)
        self.create_textbox(self.labels[1], 2)

        tk.Button(self.master, text="Download", font=("Arial", 16), command=self.download).pack(padx=10, pady=10)

    def create_textbox(self, label_text, textbox_id):
        """Creates textboxes with labels."""
        label = tk.Label(self.master, text=label_text, font=("Arial", 10))
        label.pack(padx=10, pady=5)

        textbox = tk.Text(self.master, height=1, font=("Arial", 16))
        textbox.pack(padx=10, pady=5)

        setattr(self, f"textbox{textbox_id}", textbox)

    def download(self):
        """Handles the download process."""
        playlist_url = self.textbox1.get("1.0", tk.END).strip()
        destination_path = self.textbox2.get("1.0", tk.END).strip()

        playlist = Playlist(playlist_url, client_id, client_secret)
        playlist_tracks = playlist.get_playlist_tracks()
        links = playlist.search_for_songs(playlist_tracks)
        playlist.download_mp3(links, destination_path)
