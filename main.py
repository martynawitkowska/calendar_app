from datetime import datetime
from pprint import pprint

from data_generator import DataGenerator
from event import Event

events = DataGenerator.load_data('event_data.json')
events_objects = []

for event in events:
    event['start_date'] = datetime.strptime(event['start_date'], '%Y/%m/%d, %H:%M')
    events_objects.append(Event(**event))

pprint(events_objects)
