from azure.eventgrid import EventGridClient
from msrest.authentication import TopicCredentials
import uuid
from datetime import datetime
import json

eventgrid_accesskey = input('Please enter your access key:')

credentials = TopicCredentials(eventgrid_accesskey)
event_grid_client = EventGridClient(credentials)
subject = 'traffic/01/1-bmz-406'
event_grid_client.publish_events(
    'savanh-real-time-iot.westeurope-1.eventgrid.azure.net',
    events=[{
        'id' : str(uuid.uuid4()),
        'subject' : subject,
        'data': "{'test':'test'}",
        'event_type': 'SuspectedCarDetected',
        'event_time': datetime.utcnow(),
        'data_version': 1
    }]
)
print('done')