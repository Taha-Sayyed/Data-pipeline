import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    client_credential_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp=spotipy.Spotify(client_credentials_manager=client_credential_manager)
    playlists=sp.user_playlists('spotify')

    playlist_link="https://open.spotify.com/playlist/7qxn6GsFH77ghVtKzOnAYA"
    playlist_URI=playlist_link.split("/")[-1].split("?")[0]

    spotify_data=sp.playlist_tracks(playlist_URI)
    print(spotify_data)

    client=boto3.client('s3')

    filename="spotify_raw_" + str(datetime.now()) + ".json"



    client.put_object(Body=json.dumps(spotify_data), Bucket='spotify-etl-pipeline-learning', Key='raw_data/to_processed/' + filename)
