from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv() # Automatically load environment variable files


# Fetch client_id and client_secret from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    # Combine client_id and client_secret into a single string and encode it as bytes
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")

    # Base64 encode the bytes to create the Authorization header value
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # Endpoint to request an access token
    url = "https://accounts.spotify.com/api/token"

    # Headers required for the authentication request
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Data to request a client credentials grant type for obtaining an access token
    data = {"grant_type": "client_credentials"}

    # Make a POST request to the Spotify API to get the access token
    result = post(url, headers=headers, data=data)

    # Parse the response as JSON to extract the access token
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token


def get_auth_header(token):
    # Generate the Authorization header value with the access token
    return {"Authorization": "Bearer " + token}


token = get_token()