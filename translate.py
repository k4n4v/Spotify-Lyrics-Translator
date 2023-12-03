from song import get_track
from lyrics import get_lyrics
from googletrans import Translator

translator = Translator()

def user_url():
    song_url = input("Enter Spotify song url: ")
    return song_url

def translate():
    
    song_url = user_url()
    track_name, track_artist = get_track(song_url)
    
    lyrics = get_lyrics(track_name, track_artist)
    result = translator.translate(lyrics, dest='en')
    
    print(result.text)
    
translate()