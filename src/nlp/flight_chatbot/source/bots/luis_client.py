import requests
import json
from typing import List
from .luis_models import Intent, IntentResponse, Prediction

key = ''
endpoint = 'westus.api.cognitive.microsoft.com' 
appId = ''


class LuisClient:
    
    @staticmethod
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

