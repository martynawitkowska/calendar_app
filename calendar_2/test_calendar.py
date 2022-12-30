from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from calendar_2 import Calendar
from event import Event


@pytest.fixture
def stub_events():
    stub_event_1 = Mock(Event)
    stub_event_1.start_date = datetime.now().replace(microsecond=0) + timedelta(days=3)
    stub_event_1.duration = 25
    stub_event_2 = Mock(Event)
    stub_event_2.start_date = datetime.now().replace(microsecond=0) + timedelta(weeks=5)
    stub_event_2.duration = 30
    stub_event_3 = Mock(Event)
    stub_event_3.start_date = datetime.now().replace(microsecond=0) + timedelta(days=4)
    stub_event_3.duration = 50
    stub_event_4 = Mock(Event)
    stub_event_4.start_date = datetime.now().replace(microsecond=0) + timedelta(weeks=5)
    stub_event_4.duration = 45

    return [stub_event_1, stub_event_2, stub_event_3, stub_event_4]


@pytest.fixture
def stub_event():
    event = Mock(Event)
    event.start_date = datetime.now().replace(microsecond=0) + timedelta(days=5)
    return event


def test_events_getter(stub_events):
    calendar = Calendar(stub_events)

    assert calendar.events == 'You have 2 events in four upcoming weeks.'


def test_new_event_invalid_type_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        event = 'New event of wrong type'
        calendar = Calendar()
        calendar.events = event

        assert 'should be of type Event, Workshop or Reminder' in excinfo.value


def test_add_new_event_positive(stub_events, stub_event):
    calendar = Calendar(stub_events)
    calendar.events = stub_event

    assert calendar.events == 'You have 3 events in four upcoming weeks.'


def testt_filter_method_with_duration_option(stub_events):
    calendar = Calendar(stub_events)
    sorted_events = calendar.filter('duration', min=28, max=47)

    assert sorted_events == [stub_events[1], stub_events[3]]
