import requests

SEARCH_URL = 'https://api.musixmatch.com/ws/1.1/track.search?q_track={0}&q_artist={1}&apikey=e5cc295158a91cb6a0419bdca5d661c7' # 0 title 1 artist
LYRICS_URL = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={0}&apikey=e5cc295158a91cb6a0419bdca5d661c7' # 0 track id

def get_track_id(title, artist):
    """
    Gets the ID of a track utilizing its title and the artist.
    """
    response = requests.get(SEARCH_URL.format(title, artist)).json()

    if response['message']['header']['status_code'] == 404:
        return 404

    track_id = response['message']['body']['track_list'][0]['track']['track_id']
    return track_id

def get_track_lyrics(track_id):
    """
    Gets 30% of the lyrics of a song with its id.
    """
    response = requests.get(LYRICS_URL.format(track_id)).json()

    if response['message']['header']['status_code'] == 404:
        return 404

    lyrics = response['message']['body']['lyrics']['lyrics_body'][:-75]
    return lyrics

def main():
    """
    For testing purposes.
    """
    track_id = get_track_id('ronson princess', 'clarence')
    print(get_track_lyrics(track_id))

if __name__ == '__main__':
    main()
