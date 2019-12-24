from typing import List

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
