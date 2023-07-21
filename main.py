import spot

spotify_playlist_url = input("Please enter your spotify playlist url: ")
file_destination = input("Please enter the destination where the songs will be saved at: ")
song_name = input("(IF NEEDED) Please enter the song name you want to remove from the folder (without .mp3 extension): ")

playlist1 = Playlist(spotify_playlist_url,client_id,client_secret)
tracks = playlist1.get_playlist_tracks(spotify_playlist_url,client_id,client_secret)
search = playlist1.search_for_songs(tracks)
download = playlist1.download_mp3(search, file_destination)
remove = playlist1.song_remove(song_name, file_destination)