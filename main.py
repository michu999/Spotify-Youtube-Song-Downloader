import base64
from requests import post
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
from pytube import YouTube
from youtubesearchpython import VideosSearch

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers= headers, data= data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}

def get_playlist_tracks(playlist_id, client_id, client_secret):
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
                artists_songs_dict[artist_name] = [song_name]
    return artists_songs_dict

def search_for_songs(song_dict):
    link_list = []
    for artist, songs in song_dict.items():
        for song in songs:
            song_data = f"{artist} {song}"
            search = VideosSearch(song_data,limit=1)
            results = search.result()
            link = results['result'][0]['link']
            link_list.append(link)
    return link_list

def download_mp3(list_of_links, destination):
    for link in list_of_links:
        try:
            video = YouTube(link).streams.filter(only_audio=True).first()
            output_file = video.download(output_path=destination)
            base, ext = os.path.splitext(output_file)
            new_file = base + '.mp3'
            os.rename(output_file, new_file)
            print(f"{video.title} has been successfully saved to {destination}")
        except Exception as e:
            print(f"An error occurred while downloading: {e}")

