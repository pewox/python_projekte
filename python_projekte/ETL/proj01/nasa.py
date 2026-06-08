import json
import requests

# https://eonet.gsfc.nasa.gov/docs/v2.1

limit = 100
days = 365
url = f"https://eonet.gsfc.nasa.gov/api/v2.1/events?limit={limit}&days={days}"
r = requests.get(url)
events_data = r.json()

with open('events.json', 'w') as f:
    f.write(json.dumps(events_data, indent=4))

# jetzt aus events.json den Eintrag "events" benutzen

event_list = events_data['events']

for event in event_list:
    print(event['title'])
    