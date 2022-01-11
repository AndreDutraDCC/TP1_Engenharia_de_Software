from google.cloud import language_v1
from google.oauth2 import service_account
from base64 import b64decode, b64encode
import json

def sample_analyze_sentiment(sample_text):
    """
    Receives some text and return its sentiment.
    """
    # decode the file for the api usage
    f = open('credentials.json', 'r')
    data_encoded = bytes(f.read(), 'utf-8')
    f.close()

    f = open('/tmp/credentials.json', 'w')
    f.write(str(b64decode(data_encoded))[2:-1].replace('\\n','\n').replace('\\\n','\\n'))
    f.close()

    cred = service_account.Credentials.from_service_account_file("/tmp/credentials.json")

    # creates the client
    client = language_v1.LanguageServiceClient(credentials = cred)

    # defines the type of text
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # defines the document and the econding
    document = {"content": sample_text, "type_": type_}
    encoding_type = language_v1.EncodingType.UTF8

    # calls the api to process the text
    try:
        response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    except:
        return 404

    # get overall sentiment of the input document
    return [response.document_sentiment.score, response.document_sentiment.magnitude]

def main():
    """
    For testing purposes.
    """
    text = """
    My baby smoked some, coughin'
    She said I got baby lungs
    She asked me if I got a light
    Yeah, my favorite one
    That Ronson Princess she the best
    I'd never trade for none
    I swear I got her in my pocket
    Yeah, yeah

    Well, you got this funny look, it's on your face
    You never say what's wrong
    I say fuck it, yeah it's nothin'
    I'ma play your favorite songs
    Now it's tomorrow, man
    It's crazy how the day was gone
    We know time ain't real but it's amazin'
    How we change sometimes

    I think I better spend the night
    I left Donna at your house
    Won't you hold her tight
    So her fire won't go out
    I think I'm lost forever
    There's no light to guide me now
    Where's my mother-fuckin' princess
    Oh my god

    Well I think this shit just all depends
    I think I'm on the fence
    Think I'm lacking confidence
    I'm lacking common sense
    Think 'bout what my mama said
    Said I need better friends
    """

    score, magnitude = sample_analyze_sentiment(text)

    print(u"Document sentiment score: {}".format(score))
    print(u"Document sentiment magnitude: {}".format(magnitude))

if __name__ == '__main__':
    main()
