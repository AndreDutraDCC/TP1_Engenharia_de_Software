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

def search_track(q, t_array, token):
    """
    Search for the query q on the types on the list t_array using an access token.
    Allowed types: album, track;
    """
    req = requests.get(url='https://api.spotify.com/v1/search?q='+q+'&type='+','.join(t_array)+'&market=BR',
                       headers={'Authorization': 'Bearer ' + token,
                                'Content-Type': 'application/json'})
    return req.json()

def main():
    """
    For testing purposes.
    """
    t = 'album'
    access_token = get_client_token()
    # print(access_token)
    results = search_track('artificial flavor', [t], access_token)
    # print(json.dumps(results))

    items = []

    if t == 'track':
        for track in results['tracks']['items']:
            artists_list = [x['name'] for x in track['artists']]
            spotify_url = track['external_urls']
            track_name = track['name']
            preview_url = track['preview_url']
            album_img_url = track['album']['images'][0]
            items.append({'track_name': track_name,
                          'artists_involved': artists_list,
                          'album_img_url': album_img_url,
                          'spotify_url': spotify_url,
                          'preview_url': preview_url})
        items = items[:10]
    elif t == 'album':
        for album in results['albums']['items']:
            artists_list = [x['name'] for x in album['artists']]
            spotify_url = album['external_urls']
            album_name = album['name']
            album_img_url = album['images'][0]
            items.append({'album_name': album_name,
                          'artists_involved': artists_list,
                          'album_img_url': album_img_url,
                          'spotify_url': spotify_url})
        items = items[:10]
    else:
        return "PROBLEMA"

    print(json.dumps(items))

if __name__ == '__main__':
    main()
