from Class_Playlist import Playlist
from Class_GUI import GUI

# Create a GUI instance and run the Tkinter main loop to get user inputs
root = tk.Tk()
root.geometry("400x400")
root.title("Spotify Youtube Downloader")
label = tk.Label(root, text="Spotify Youtube Downloader", font=("Arial", 18))
label.pack(padx=10, pady=10)

gui1 = GUI(root)
gui1.playlist_texbox()
gui1.destination_textbox()
gui1.button()

root.mainloop()

# Retrieve the user inputs from the GUI
spotify_playlist_url = gui1.textbox1.get("1.0", tk.END).strip()
file_destination = gui1.textbox2.get("1.0", tk.END).strip()
#song_name = input("(IF NEEDED) Please enter the song name you want to remove from the folder (without .mp3 extension): ")

# Extract the playlist ID from the URL
playlist_id = extract_playlist_id(spotify_playlist_url)

# Check if the playlist ID is valid before proceeding
if playlist_id:
    playlist1 = Playlist(playlist_id, client_id, client_secret)
    tracks = playlist1.get_playlist_tracks()  # Only pass the playlist ID here, not other arguments
    search = playlist1.search_for_songs(tracks)
    download = playlist1.download_mp3(search, file_destination)
    remove = playlist1.song_remove(song_name, file_destination)
