from auth_token import *
from requests import get

def get_track(track_url = None):
    
    track_id = track_url.split('/')[-1].split('?')[0]
    query_url = f"https://api.spotify.com/v1/tracks/{track_id}"
    token = get_token()
    headers = get_auth_header(token)
    
    response = get(query_url, headers=headers)
    json_response = json.loads(response.content)
    
    if response.status_code == 200:      
        track_artist = json_response["artists"][0]["name"]
        track_name = json_response["name"]
    else:
        print("Track not found")
        exit()

    return track_name, track_artist
