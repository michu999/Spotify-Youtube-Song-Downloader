import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from youtubesearchpython import VideosSearch

class Playlist:
    def __init__(self, playlist_id, client_id, client_secret):
        self.playlist_id = playlist_id
        self.client_id = client_id
        self.client_secret = client_secret
        load_dotenv()

    def get_playlist_tracks(self):
        """Uses Spotify's API to create a dictionary of songs in a given playlist."""
        auth_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.playlist_tracks(self.playlist_id)
        artists_songs_dict = {}
        for item in results['items']:
            track = item['track']
            artist_names = [artist['name'] for artist in track['artists']]
            song_name = track['name']
            for artist_name in artist_names:
                artists_songs_dict.setdefault(artist_name, []).append(song_name)
        return artists_songs_dict

    def search_for_songs(self, song_dict):
        """Uses the song dictionary to search for YouTube links."""
        link_list = []
        for artist, songs in song_dict.items():
            for song in songs:
                song_data = f"{artist} {song}"
                search = VideosSearch(song_data, limit=1)
                results = search.result()
                link = results['result'][0]['link']
                link_list.append(link)
        return link_list

    def download_mp3(self, list_of_links, destination):
        """Downloads MP3 files from YouTube using the provided links."""
        for link in list_of_links:
            try:
                video = YouTube(link).streams.filter(only_audio=True).first()
                output_file = video.download(output_path=destination)
                new_file = os.path.splitext(output_file)[0] + '.mp3'
                if not os.path.exists(new_file):
                    os.rename(output_file, new_file)
                    print(f"{video.title} has been successfully saved to {destination}")
                else:
                    os.remove(output_file)
                    print(f"{video.title} already exists in: {destination}")
            except Exception as e:
                print(f"An error occurred while downloading: {e}")

    def song_remove(self, song_name, destination):
        """Removes a song from the designated folder."""
        full_destination = os.path.join(destination, f"{song_name}.mp3")
        if os.path.exists(full_destination):
            os.remove(full_destination)
            print(f"{song_name} removed from {destination}")
        else:
            print(f"{song_name} doesn't exist in: {destination}")

# Load credentials from environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
