from auth_token import *
from requests import get

def get_track(token):
    
    track_url = "https://open.spotify.com/track/5BbdKBZO0TH0GhfxUfyhL9?si=b86d27044c19481b"
    track_id = track_url.split('/')[-1].split('?')[0]
    
    query_url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    
    if result.status_code == 200:      
        track_artist = json_result["artists"][0]["name"]
        track_name = json_result["name"]
    else:
        print("Track not found")

    return track_name, track_artist

def get_lyrics(track_name, track_artist):
    print(track_artist, track_name)

def translate():
    
    token = get_token()
    track_name, track_artist = get_track(token)
    get_lyrics(track_name, track_artist)


translate()
    
    