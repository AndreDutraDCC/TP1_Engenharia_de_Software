import requests
import json
from base64 import b64encode

client_id = '3daeddc98fd94f57aed5e2e65c3b385f'
client_secret = '91fec090870346b594e859eff6c2744c'

def get_client_token():
    """
    Get our respective Spotify client token.
    """
    secret = client_id + ':' + client_secret
    based_secret = str(b64encode(secret.encode('utf-8')),'utf-8')
    req = requests.post(url='https://accounts.spotify.com/api/token',
                        data='grant_type=client_credentials',
                        headers={'Content-Type': 'application/x-www-form-urlencoded',
                                 'Authorization': 'Basic ' + based_secret})

    return req.json()['access_token']

def search_track(q, token):
    """
    Search for the query q on the types on the list t_array using an access token.
    Allowed types: album, track;
    """
    req = requests.get(url='https://api.spotify.com/v1/search?q='+q+'&type=track&market=BR',
                       headers={'Authorization': 'Bearer ' + token,
                                'Content-Type': 'application/json'})
    return req.json()

def parse_results(results):
    """
    Receives a list of dictionaries that represent tracks and format them.
    """
    ret = []

    for track in results['tracks']['items']:
        artists_list = [x['name'] for x in track['artists']]
        spotify_url = track['external_urls']
        track_name = track['name']
        preview_url = track['preview_url']
        album_img_url = track['album']['images'][0]
        ret.append({'track_name': track_name,
                    'artists_involved': artists_list,
                    'album_img_url': album_img_url,
                    'external_urls': spotify_url,
                    'preview_url': preview_url})
    ret = ret[:20]

    return ret

def main():
    """
    For testing purposes.
    """
    access_token = get_client_token()
    results = search_track('ronson princess', access_token)
    print(json.dumps(parse_results(results)))

if __name__ == '__main__':
    main()
