import lyricsgenius
import os

from dotenv import load_dotenv

load_dotenv()
client_access_token = os.getenv("CLIENT_ACCESS_TOKEN_GENIUS")
genius = lyricsgenius.Genius(client_access_token)

def get_lyrics(track_name, track_artist):
    song = genius.search_song(track_name, track_artist)
    return song.lyrics
