from sentiment import sample_analyze_sentiment
from spotify import get_client_token, search_track, parse_results
from musixmatch import get_track_id, get_track_lyrics
import json

def main(event, context):
    """
    Receives a keyword and returns a dictionary list, with each list element
    representing a track from Spotify.
    """
    ret = []

    # gets the keyword searched
    keyword = json.loads(event['body'])['keyword']

    # search for keyword in spotify api
    access_token = get_client_token()
    results = search_track(keyword, access_token)
    track_list = parse_results(results)

    if len(track_list) == 0:
        return {'message': 'No track returned from that query.'}

    for track in track_list:
        # search for lyrics in musixmatch api using title and artist
        title = track['track_name']
        artist = track['artists_involved'][0]

        track_id = get_track_id(title, artist)
        if track_id == 404:
            track['sentiment'] = {'message': 'Couldn\'t find the track in Musixmatch API'}
            ret.append(track)
            continue

        text = get_track_lyrics(track_id)
        if text == 404:
            track['sentiment'] = {'message': 'Couldn\'t find the lyrics in Musixmatch API'}
            ret.append(track)
            continue

        # get the track sentiment with google cloud language api
        score, magnitude = sample_analyze_sentiment(text)

        # adds the information to the track info and adds it all to the
        # return list
        track['sentiment'] = {'score': score, 'magnitude': magnitude}
        ret.append(track)

    return {'track_list': ret}

    return response
