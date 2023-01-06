import json
from datetime import datetime, timedelta, date
from unittest.mock import Mock

import pytest

from calendar_2 import Calendar
from data_generator import DataGenerator
from event import Event, Workshop


@pytest.fixture
def event():
    return Event(1, datetime.now().replace(microsecond=0) + timedelta(hours=3), 20, '', '', '')


@pytest.fixture
def stub_events():
    stub_event_1 = Mock(Event, idx=1, title='event 1', description='Very interesting description', owner='John')
    stub_event_1.start_date = datetime.now().replace(microsecond=0) + timedelta(days=3)
    stub_event_1.duration = 25
    stub_event_2 = Mock(Event, idx=2, title='event 2', description='Another interesting story', owner='John')
    stub_event_2.start_date = datetime.now().replace(microsecond=0) + timedelta(weeks=5)
    stub_event_2.duration = 30
    stub_event_3 = Mock(Event, idx=3, title='meeting 3', description='Meet with John', owner='Mary')
    stub_event_3.start_date = datetime.now().replace(microsecond=0) + timedelta(days=4)
    stub_event_3.duration = 50
    stub_event_4 = Mock(Event, idx=4, title='event 4', description='This is another thing', owner='Mary')
    stub_event_4.start_date = datetime.now().replace(microsecond=0) + timedelta(weeks=5)
    stub_event_4.duration = 45

    return [stub_event_1, stub_event_2, stub_event_3, stub_event_4]


@pytest.fixture
def stub_workshops():
    stub_date = datetime.now().replace(microsecond=0)
    stub_workshop_1 = Mock(Workshop, start_date=stub_date + timedelta(days=3),
                           participants=['Emily', 'John', 'Mary', 'George'])
    stub_workshop_2 = Mock(Workshop, start_date=stub_date + timedelta(days=8),
                           participants=['Misha', 'Adam', 'Anna', 'Kate'])
    stub_workshop_3 = Mock(Workshop, start_date=stub_date + timedelta(weeks=5),
                           participants=['Emily', 'Adam', 'Anna', 'Kate'])
    stub_workshop_4 = Mock(Workshop, start_date=stub_date + timedelta(days=7),
                           participants=['George', 'John', 'Adam', 'Kate'])

    return [stub_workshop_1, stub_workshop_2, stub_workshop_3, stub_workshop_4]


@pytest.fixture
def stub_event():
    event = Mock(Event)
    event.start_date = datetime.now().replace(microsecond=0) + timedelta(days=5)
    return event


@pytest.fixture
def calendar(stub_events):
    return Calendar(stub_events)


@pytest.fixture
def data_generator_workshop_false():
    return DataGenerator(
                beginning_date=date.today() + timedelta(days=12),
                durations=(15, 180),
                titles=['lunch', 'lecture'],
                descriptions=['nice event', 'some meeting'],
                users=['Mister Someone', 'John'],
                reminder=True,
                workshop=False)


@pytest.fixture
def data_generator_workshop_true():
    return DataGenerator(
                beginning_date=date.today() + timedelta(days=12),
                durations=(15, 180),
                titles=['lunch', 'lecture'],
                descriptions=['nice event', 'some meeting'],
                users=['Mister Someone', 'John'],
                reminder=False,
                workshop=True)


@pytest.fixture
def test_events_path(tmp_path):
    date = datetime.now().replace(microsecond=0) + timedelta(days=3)
    test_event_json = [{"idx": 0,
                        "start_date": f"{date:%Y/%m/%d, %H:%M}",
                        "duration": 154,
                        "title": "lunch",
                        "description": "nice event",
                        "owner": "Mister Someone"}]
    test_reminder_json = [{"idx": 3,
                           "start_date": f"{date:%Y/%m/%d, %H:%M}",
                           "duration": 151,
                           "title": "sport event",
                           "description": "some meeting",
                           "owner": "Another Person",
                           "remind": True}]
    test_workshop_json = [{"idx": 5,
                           "start_date": f"{date:%Y/%m/%d, %H:%M}",
                           "duration": 27,
                           "title": "lecture",
                           "description": "some meeting",
                           "owner": "Happy Person",
                           "participants": ["Wojtek", "Zdzisiek"]}]
    path = tmp_path / 'test_directory'
    path.mkdir()

    file_1 = path / 'event_data.json'
    file_1.write_text(json.dumps(test_event_json))

    file_2 = path / 'reminder_data.json'
    file_2.write_text(json.dumps(test_reminder_json))

    file_3 = path / 'workshop_data.json'
    file_3.write_text(json.dumps(test_workshop_json))

    return path
