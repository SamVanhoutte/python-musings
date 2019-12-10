import requests
import json
from typing import List

key = ''
endpoint = 'westus.api.cognitive.microsoft.com' 
appId = ''


class Intent(object):
    def __init__(self, intent: str, score: float):
        self.intent = intent
        self.score = score

class Prediction(object):
    def __init__(self, topIntent: str, intents: List[Intent], entities: dict):
        self.topIntent = topIntent
        self.intents = intents
        self.entities = entities

    @classmethod
    def from_json(cls, data):
        topIntent = data['topIntent']
        entities = dict(data['entities'])
        intents = list()
        intent_dict = dict(data["intents"])
        for intent_name in intent_dict.keys():
            intents.append(Intent(intent_name, intent_dict[intent_name]['score']))

        return cls(topIntent, intents, entities)

class IntentResponse(object):
    def __init__(self, query, prediction):
        self.prediction = prediction
        self.query = query

    @classmethod
    def from_json(cls, data):
        query = data["query"]
        prediction = Prediction.from_json(data["prediction"])
        return cls(query, prediction)

def getIntent(utterance:str, key:str, endpoint:str, appId:str, debug=False) -> IntentResponse:
    try:
        headers = {
        }

        params ={
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'false',
            'show-all-intents': 'false',
            'spellCheck': 'false',
            'staging': 'true',
            'subscription-key': key
        }

        r = requests.get(f'https://{endpoint}/luis/prediction/v3.0/apps/{appId}/slots/staging/predict',headers=headers, params=params)
        result = r.json()
        intentResponse = IntentResponse.from_json(result)
        if debug:
            print('==========================================')
            print(intentResponse.query)
            print('Top intent:', intentResponse.prediction.topIntent)
            print('Probability score:', intentResponse.prediction.intents[0].score)
            print('Detected entities:', intentResponse.prediction.entities)
        return intentResponse
        
    except Exception as e:
        print(f'{e}')

def handleFlightBooking(intent: IntentResponse):
    # Handle specific flight request
    # Verify if there is an origin airport in the entities
    if not('Origin' in intent.prediction.entities):
        origin = input('Please enter your origin aiport:')
    else:
        origin = intent.prediction.entities['Origin'][0][0]
    if not('Destination' in intent.prediction.entities):
        destination = input('Please enter your destination aiport:')
    else:
        destination = intent.prediction.entities['Destination'][0][0]
    print('Your flight from', origin, 'to', destination, 'has been booked')

def handleRequest(utterance:str, key:str, endpoint:str, appId:str, debug=False):
    #Verify intent
    intent = getIntent(utterance, key, endpoint, appId, debug)
    if intent.prediction.topIntent=='travel.flight':
        handleFlightBooking(intent)
    else:
        print('The intent', intent.prediction.topIntent, 'is not supported by this program')
    return 


debug_flag = True
handleRequest('Ik wil een vlucht boeken van Kortrijk naar Luik',key,endpoint,appId,debug_flag)
handleRequest('Ik wil een vlucht boeken naar Luik',key,endpoint,appId,False)
handleRequest('Ik wil een vlucht boeken van Kortrijk',key,endpoint,appId,False)
