import json
from requests import get
from spotify_auth import token, get_auth_header
import csv

"""rap_playlists = [
"https://open.spotify.com/playlist/37i9dQZF1DWSMW5YBCZisa?si=feca8934af1841ce", # 2010
"https://open.spotify.com/playlist/37i9dQZF1DX3D1xvN8LjbH?si=eafcae448b4e4786", # 2011
"https://open.spotify.com/playlist/37i9dQZF1DX92DV8EP7bwz?si=bd3fa40cfcbb4e59", # 2012
"https://open.spotify.com/playlist/37i9dQZF1DWSWuGRBgXzLE?si=d5752c928ede42ee", # 2013
"https://open.spotify.com/playlist/37i9dQZF1DWTOgTfzyNaei?si=49508de254154108", # 2014
"https://open.spotify.com/playlist/37i9dQZF1DXcqWbpeXswkc?si=f2ef06f647bf430c", # 2015
"https://open.spotify.com/playlist/37i9dQZF1DWZSCnPqfx5XX?si=207df2c122b54912", # 2016
"https://open.spotify.com/playlist/37i9dQZF1DWUUeLChAs7Px?si=edc3160b4d394499", # 2017
"https://open.spotify.com/playlist/37i9dQZF1DWVXS1PI6Zs44?si=6af0862dbc044171", # 2018
"https://open.spotify.com/playlist/37i9dQZF1DWZiyat8YCzeB?si=b337a7d496804275", # 2019
]

pop_playlists = [
"https://open.spotify.com/playlist/5SETelP2vUEJDSpK93lXpr?si=e655e7c1c3fc4d8b", # 2010
"https://open.spotify.com/playlist/2KDeIbzjfPtE8gNruQl7tY?si=a01ee50edc6e4b82", # 2011
"https://open.spotify.com/playlist/7caceCufp0UbcOWejFkDoj?si=b831984ecb824ee4", # 2012
"https://open.spotify.com/playlist/2KDeIbzjfPtE8gNruQl7tY?si=768ab064e4c74d32", # 2013
"https://open.spotify.com/playlist/7caceCufp0UbcOWejFkDoj?si=19d4cb6513b14e75", # 2014
"https://open.spotify.com/playlist/1boDB6Ev3gYm04lJ6qPTDR?si=5b4c84f091f742fd", # 2015
"https://open.spotify.com/playlist/1GLsDSHiAiFVsaB13n2b80?si=001eaa23bf9d4291", # 2016
"https://open.spotify.com/playlist/4hnnIp3xnVDlY50javmPN9?si=e99fc07ec2a848d0", # 2017
"https://open.spotify.com/playlist/7hj70MyCSV0rP4xr0R3GBx?si=93ea0cdfca774ece", # 2018
"https://open.spotify.com/playlist/4Ni1b2rQAtpURFDM1MLzbJ?si=8bd60e59cbb54c31", # 2019
]
"""
top_playlists = [
"https://open.spotify.com/playlist/37i9dQZF1DWXQyLTHGuTIz?si=9a6895d3be5a4222", # 1970
"https://open.spotify.com/playlist/37i9dQZF1DX43B4ApmA3Ee?si=f2621aafd77a4723", # 1971
"https://open.spotify.com/playlist/37i9dQZF1DXaQBa5hAMckp?si=ae3e48da7443408d", # 1972
"https://open.spotify.com/playlist/37i9dQZF1DX2ExTChOnD3g?si=f7bdbb0c546e4d67", # 1973
"https://open.spotify.com/playlist/37i9dQZF1DWVg6L7Yq13eC?si=52eed0e931214a18", # 1974
"https://open.spotify.com/playlist/37i9dQZF1DX3TYyWu8Zk7P?si=a96ebc9ea9c64337", # 1975
"https://open.spotify.com/playlist/37i9dQZF1DX6rhG68uMHxl?si=25c4ce84099b4de8", # 1976
"https://open.spotify.com/playlist/37i9dQZF1DX26cozX10stk?si=4b1f62d3c26540ec", # 1977
"https://open.spotify.com/playlist/37i9dQZF1DX0fr2A59qlzT?si=70435fcd65574f0f", # 1978
"https://open.spotify.com/playlist/37i9dQZF1DWZLO9LcfSmxX?si=c4034121037941c9", # 1979
"https://open.spotify.com/playlist/37i9dQZF1DWXbLOeOIhbc5?si=b6bb5a13aebc42df", # 1980
"https://open.spotify.com/playlist/37i9dQZF1DX3MaR62kDrX7?si=13bda13382584f42", # 1981
"https://open.spotify.com/playlist/37i9dQZF1DXas7qFgKz9OV?si=bc2dbb06eaa7442a", # 1982
"https://open.spotify.com/playlist/37i9dQZF1DXbE3rNuDfpVj?si=8801d4a91ad94262", # 1983
"https://open.spotify.com/playlist/37i9dQZF1DX2O7iyPnNKby?si=83258c50427a42c5", # 1984
"https://open.spotify.com/playlist/37i9dQZF1DWXZ5eJ1sVtmf?si=fdacb18f50144493", # 1985
"https://open.spotify.com/playlist/37i9dQZF1DX7b12kdMQTpG?si=d844b9d94fdc45a1", # 1986
"https://open.spotify.com/playlist/37i9dQZF1DX38yySwWsFRT?si=12829a5bc5ad4d59", # 1987
"https://open.spotify.com/playlist/37i9dQZF1DX3MZ9dVGvZnZ?si=14c46290c953449b", # 1988
"https://open.spotify.com/playlist/37i9dQZF1DX4qJrOCfJytN?si=329f9ecbf47140ba", # 1989
"https://open.spotify.com/playlist/37i9dQZF1DX4joPVMjBCAo?si=2c1aa65f36394ac9", # 1990
"https://open.spotify.com/playlist/37i9dQZF1DX6TtJfRD994c?si=8b6cd840c6384025", # 1991
"https://open.spotify.com/playlist/37i9dQZF1DX9ZZCtVNwklG?si=77314c5e6d6c4014", # 1992
"https://open.spotify.com/playlist/37i9dQZF1DXbUFx5bcjwWK?si=4b006718573c4d75", # 1993
"https://open.spotify.com/playlist/37i9dQZF1DXbKFudfYGcmj?si=e62721750bfa4edd", # 1994
"https://open.spotify.com/playlist/37i9dQZF1DXayIOFUOVODK?si=9d8d61145faa404f", # 1995
"https://open.spotify.com/playlist/37i9dQZF1DWZkDl55BkJmo?si=c64f831b69324432", # 1996
"https://open.spotify.com/playlist/37i9dQZF1DWWKd15PHZNnl?si=b9a190cd35c1434e", # 1997
"https://open.spotify.com/playlist/37i9dQZF1DWWmGB2u14f8m?si=a44f0dd731594b1c", # 1998
"https://open.spotify.com/playlist/37i9dQZF1DX4PrR66miO50?si=990d2ce4e8c8471f", # 1999
"https://open.spotify.com/playlist/37i9dQZF1DWUZv12GM5cFk?si=304f64c1cbd14c57", # 2000
"https://open.spotify.com/playlist/37i9dQZF1DX9Ol4tZWPH6V?si=e763c05d97cd4fbe", # 2001
"https://open.spotify.com/playlist/37i9dQZF1DX0P7PzzKwEKl?si=fddb56e226b64ab7", # 2002
"https://open.spotify.com/playlist/37i9dQZF1DXaW8fzPh9b08?si=755c80dd38074671", # 2003
"https://open.spotify.com/playlist/37i9dQZF1DWTWdbR13PQYH?si=e0e47e3ab05c45bf", # 2004
"https://open.spotify.com/playlist/37i9dQZF1DWWzQTBs5BHX9?si=3b675643be374a19", # 2005
"https://open.spotify.com/playlist/37i9dQZF1DX1vSJnMeoy3V?si=e52e38d205b54f69", # 2006
"https://open.spotify.com/playlist/37i9dQZF1DX3j9EYdzv2N9?si=032ad0b195d448b7", # 2007
"https://open.spotify.com/playlist/37i9dQZF1DWYuGZUE4XQXm?si=2d879d0671894d0c", # 2008
"https://open.spotify.com/playlist/37i9dQZF1DX4UkKv8ED8jp?si=e136ccb52f1f4bc8", # 2009
"https://open.spotify.com/playlist/37i9dQZF1DXc6IFF23C9jj?si=188eb5f59f7645c3", # 2010
"https://open.spotify.com/playlist/37i9dQZF1DXcagnSNtrGuJ?si=5926120f240e4ed8", # 2011
"https://open.spotify.com/playlist/37i9dQZF1DX0yEZaMOXna3?si=7c5abfeb86654283", # 2012
"https://open.spotify.com/playlist/37i9dQZF1DX3Sp0P28SIer?si=2d6b3a7589f6411d", # 2013
"https://open.spotify.com/playlist/37i9dQZF1DX0h0QnLkMBl4?si=83f8ffe63155439b", # 2014
"https://open.spotify.com/playlist/37i9dQZF1DX9ukdrXQLJGZ?si=8c6ea8706b4f401d", # 2015
"https://open.spotify.com/playlist/37i9dQZF1DX8XZ6AUo9R4R?si=4b4bc3d22c9b453c", # 2016
"https://open.spotify.com/playlist/37i9dQZF1DWTE7dVUebpUW?si=fe723feb4feb4594", # 2017
"https://open.spotify.com/playlist/37i9dQZF1DXe2bobNYDtW8?si=e0524141064445b3", # 2018
"https://open.spotify.com/playlist/37i9dQZF1DWVRSukIED0e9?si=eea9506b3df946fe", # 2019
]


def get_playlist_tracks(token, playlist_id):
    # COPY LAST PART AFTER playlist/ FOR PLAYLIST ID
    # https://open.spotify.com/playlist/37i9dQZF1DWSJEMFaWwYG8?si=80f4b1f105054776
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]

    playlist_tracks = []

    for track in json_result:
        track_info = {
            'id': track["track"]["id"],
            'name': track["track"]["name"],
            'artist': track["track"]["artists"][0]["name"],
            'popularity': track["track"]["popularity"], 
            'explicit': track["track"]["explicit"]
        }
        playlist_tracks.append(track_info)

    return playlist_tracks


"""def add_track_features(token, playlist_tracks):
    url = f"https://api.spotify.com/v1/audio-features"
    query = "?ids="
    headers = get_auth_header(token)

    track_ids = [track['id'] for track in playlist_tracks]

    for i, track_id in enumerate(track_ids):
        query_url = url + query + track_id
        result = get(query_url, headers=headers)

        track_features = json.loads(result.content)["audio_features"][0]
        
        playlist_tracks[i]['energy'] = track_features["energy"]
        # playlist_tracks[i]['id_2'] = track_features["id"] # DOUBLE CHECK IF ID's MATCH UP
        playlist_tracks[i]['tempo'] = track_features["tempo"]
        playlist_tracks[i]['positiveness'] = track_features["valence"]
        playlist_tracks[i]['danceability'] = track_features["danceability"]
        playlist_tracks[i]['acousticness'] = track_features["acousticness"]
        playlist_tracks[i]['instrumentalness'] = track_features["instrumentalness"]
        playlist_tracks[i]['loudness'] = track_features["loudness"]
        playlist_tracks[i]['mode'] = track_features["mode"]
        playlist_tracks[i]['speechiness'] = track_features["speechiness"]

    
    return playlist_tracks"""

def add_track_features(token, playlist_tracks):
    url = f"https://api.spotify.com/v1/audio-features"
    query = "?ids="
    headers = get_auth_header(token)

    track_ids = [track['id'] for track in playlist_tracks]

    for i, track_id in enumerate(track_ids):
        query_url = url + query + track_id
        result = get(query_url, headers=headers)

        track_features_data = json.loads(result.content)["audio_features"]
        
        # check if track_features is not None
        if not track_features_data or track_features_data[0] is None:
            print(f"Warning: No features found for track with ID: {track_id}")
            # set default values
            track_features = {
                "energy": 0.0,
                "tempo": 0.0,
                "valence": 0.0,
                "danceability": 0.0,
                "acousticness": 0.0,
                "instrumentalness": 0.0,
                "loudness": 0.0,
                "mode": 0,
                "speechiness": 0.0,
                "duration_ms": 0,  
                "key": -1  
            }
        else:
            track_features = track_features_data[0]
        
        playlist_tracks[i]['energy'] = track_features["energy"]
        # playlist_tracks[i]['id_2'] = track_features["id"] # DOUBLE CHECK IF ID's MATCH UP
        playlist_tracks[i]['tempo'] = track_features["tempo"]
        playlist_tracks[i]['positiveness'] = track_features["valence"]
        playlist_tracks[i]['danceability'] = track_features["danceability"]
        playlist_tracks[i]['acousticness'] = track_features["acousticness"]
        playlist_tracks[i]['instrumentalness'] = track_features["instrumentalness"]
        playlist_tracks[i]['loudness'] = track_features["loudness"]
        playlist_tracks[i]['mode'] = track_features["mode"]
        playlist_tracks[i]['speechiness'] = track_features["speechiness"]
        playlist_tracks[i]['duration_ms'] = track_features["duration_ms"]
        playlist_tracks[i]['key'] = track_features["key"]

    return playlist_tracks




def get_track_info(token, playlist_tracks):
    url = f"https://api.spotify.com/v1/tracks/"
    headers = get_auth_header(token)

    track_ids = [track['id'] for track in playlist_tracks]

    for i, track_id in enumerate(track_ids):
        query_url = url + track_id
        result = get(query_url, headers=headers)

        track_info = json.loads(result.content)["album"]
        
        playlist_tracks[i]['album_name'] = track_info["name"]
        
    return playlist_tracks


playlist_ids = [i[34:] for i in top_playlists] # <- Change playlist name to correct playlist!
years = list(range(1970, 2020)) # list of years corresponding to the order of playlists
all_playlist_data = [] # list to store data from all playlists


for idx, (playlist_id, year) in enumerate(zip(playlist_ids, years), start=1):
    print(f"Processing playlist {idx}/{len(playlist_ids)} - Playlist ID: {playlist_id}")
    
    playlist_tracks = get_playlist_tracks(token, playlist_id)
    print(f"Fetched playlist tracks - {len(playlist_tracks)} tracks")
    
    new_dict = add_track_features(token, playlist_tracks)
    print("Added track features")
    
    new_dict_2 = get_track_info(token, new_dict)
    print("Added track info")

    # append the 'year' information to each track's data dictionary
    for track_data in new_dict_2:
        track_data['year'] = year

    # accumulate data from each playlist into the all_playlist_data list
    all_playlist_data.extend(new_dict_2)
    print("Extended list of playlists")

def export_to_csv(data, filename):
    # define field names (column headers) for the CSV file
    field_names = data[0].keys()  # all dictionaries have same keys

    # write data to CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

export_to_csv(all_playlist_data, '../data/top_hits_1970_to_2019_real.csv') # <- Change csv filename
