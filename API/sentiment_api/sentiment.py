from google.cloud import language_v1
from google.oauth2 import service_account
import json

def sample_analyze_sentiment(sample_text):
    with open("credentials.json") as f:
        info = json.load(f) 

    cred = service_account.Credentials.from_service_account_file("credentials.json")
    client = language_v1.LanguageServiceClient(credentials = cred)

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    #language = "en"
    
    document = {"content": sample_text, "type_": type_}

    # Available values: NONE, UTF8, UTF16, UTF32

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

sample_analyze_sentiment("Tenha boas férias!")