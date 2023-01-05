import datetime

from event import Event
from helpers import generate_objects


def test_generate_objects_with_event_data(test_events_path, monkeypatch):
    monkeypatch.chdir(test_events_path)
    date = datetime.datetime.now().replace(microsecond=0, second=0) + datetime.timedelta(days=3)
    generated_objects = generate_objects()
    assert repr(generated_objects[0]) == repr(
        Event(idx=0, owner='Mister Someone', description='nice event', title='lunch', duration=154, start_date=date))
