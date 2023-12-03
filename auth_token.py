import os
import base64
import json

from dotenv import load_dotenv
from requests import post

load_dotenv()
client_id = os.getenv("CLIENT_ID_SPOTIFY")
client_secret = os.getenv("CLIENT_SECRET_SPOTIFY")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    
    response = post(url, headers=headers, data=data)
    json_response = response.json()
    token = json_response["access_token"]
    
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
