'''
Module containing the function sentiment_analyzer
Function makes request to AI Library
'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''
    Sends text to AI Analyzer
    Formats the response for displaying required output
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers = header, timeout = 5)
    formatted_response = json.loads(response.text)
    label = ''
    score = ''
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
