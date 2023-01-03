from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from calendar_2 import Calendar
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
