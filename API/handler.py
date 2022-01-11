from sentiment import sample_analyze_sentiment
from spotify import get_client_token, search_track, parse_results
from musixmatch import get_track_id, get_track_lyrics
from base64 import b64decode
from handle_db import get_view, set_novo_sentimento, set_nova_pesquisa, set_novo_acesso
import json

def db(event, context):
    """
    Receives which kind of action it wants to do with the database and the necessary data.
    """
    response = {}
    action = json.loads(b64decode(event['body'] + b'=' * (-len(event['body']) % 4)))['action']

    if action == 'pega_visao':
        response['dados'] = get_view()
    else:
        data = json.loads(b64decode(event['body']))['data']

        if action == 'novo_sentimento':
            set_novo_sentimento(data)
        elif action == 'novo_acesso':
            set_novo_acesso(data)
        elif action == 'nova_pesquisa':
            set_nova_pesquisa(data)
        else:
            reponse['message'] = 'Couldn\'t find the requested action.'

    response["headers"] = {'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True}
    return response

def main(event, context):
    """
    Receives a keyword and returns a dictionary list, with each list element
    representing a track from Spotify.
    """
    response = {}
    ret = []

    # gets the keyword searched
    keyword = json.loads(b64decode(event['body']))['keyword']

    # search for keyword in spotify api
    access_token = get_client_token()
    results = search_track(keyword, access_token)
    track_list = parse_results(results)

    if len(track_list) == 0:
        response['message'] = 'No track returned from that query.'
        response["headers"] = {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True}
        response['track_list'] = ret
        return reponse

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
        result = sample_analyze_sentiment(text)
        if result == 404:
            track['sentiment'] = {'message': 'Couldn\'t find the lyrics in Musixmatch API'}
            ret.append(track)
            continue

        score = result[0]
        magnitude = result[1]

        # adds the information to the track info and adds it all to the
        # return list
        track['sentiment'] = {'score': score, 'magnitude': magnitude}
        ret.append(track)

    response["headers"] = {'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True}
    response['track_list'] = ret

    return response
