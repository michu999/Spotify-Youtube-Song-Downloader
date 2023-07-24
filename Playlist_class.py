import base64
from requests import post
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import pytube
from pytube import YouTube
from youtubesearchpython import VideosSearch


class Playlist():
    def __init__(self, playlist_id, client_id, client_secret):
        self.playlist_id = playlist_id
        self.client_id = client_id
        self.client_secret = client_secret

    #  Uses spotify's API to create a dictionary of songs in a given playlist
    def get_playlist_tracks(self, playlist_id, client_id, client_secret):
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.playlist_tracks(playlist_id)
        artists_songs_dict = {}
        for item in results['items']:
            track = item['track']
            artist_names = [artist['name'] for artist in track['artists']]
            song_name = track['name']
            for artist_name in artist_names:
                if artist_name in artists_songs_dict:
                    artists_songs_dict[artist_name].append(song_name)
                else:
                    artists_songs_dict[artist_name] = [song_name]  #  Assigns the artist key to a list of songs (values)
        return artists_songs_dict

    #  Uses the return value of the previous function to create a list of values ["artist song"]
    def search_for_songs(self, song_dict):
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
        for link in list_of_links:
            try:
                video = YouTube(link).streams.filter(only_audio=True).first()
                output_file = video.download(output_path=destination)
                base, ext = os.path.splitext(output_file)
                new_file = base + '.mp3'
                if not os.path.exists(new_file):
                    os.rename(output_file, new_file)
                    print(f"{video.title} has been successfully saved to {destination}")
                else:
                    os.remove(output_file) #  Removes the duplicate song
                    print(f"{video.title} already exists in: {destination}")
            except Exception as e:
                print(f"An error occurred while downloading: {e}")

    #  Allows the user to remove a song from the designated folder
    def song_remove(self, song_name, destination):
        full_destination = destination + "\\" + song_name + ".mp3"
        print(full_destination)
        if not os.path.exists(full_destination):
            print(f"{song_name} doesn't exist in: {destination}")
        else:
            os.remove(full_destination)

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
