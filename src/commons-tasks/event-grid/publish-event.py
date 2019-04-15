from datetime import datetime as dt
from urllib import request, parse
import json

eventgrid_topic = 'https://savanh-real-time-iot.westeurope-1.eventgrid.azure.net/api/events'
eventgrid_auth_key = 'dNNKXTgaLe0D/04xYpUDLaue35r/5f80V4tAlCstkug='

print(eventgrid_topic)
data = dict(licensePlate='1-BMZ-406')
encoded_data = parse.urlencode(data)
encoded_data = encoded_data.encode('utf-8')

req = request.Request('https://enrxym4wb0y3.x.pipedream.net', data=encoded_data) # this will make the method "POST"
req.add_header('Content-Type', 'application/json')
request.urlopen(req)