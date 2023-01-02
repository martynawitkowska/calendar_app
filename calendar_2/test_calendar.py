from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from calendar_2 import Calendar
from event import Event


@pytest.fixture
def stub_events():
    stub_event_1 = Mock(Event, title='event 1', description='Very interesting description')
    stub_event_1.start_date = datetime.now().replace(microsecond=0) + timedelta(days=3)
    stub_event_1.duration = 25
    stub_event_2 = Mock(Event, title='event 2', description='Another interesting story')
    stub_event_2.start_date = datetime.now().replace(microsecond=0) + timedelta(weeks=5)
    stub_event_2.duration = 30
    stub_event_3 = Mock(Event, title='meeting 3', description='Meet with John')
    stub_event_3.start_date = datetime.now().replace(microsecond=0) + timedelta(days=4)
    stub_event_3.duration = 50
    stub_event_4 = Mock(Event, title='event 4', description='This is another thing')
    stub_event_4.start_date = datetime.now().replace(microsecond=0) + timedelta(weeks=5)
    stub_event_4.duration = 45

    return [stub_event_1, stub_event_2, stub_event_3, stub_event_4]


@pytest.fixture
def stub_event():
    event = Mock(Event)
    event.start_date = datetime.now().replace(microsecond=0) + timedelta(days=5)
    return event


@pytest.fixture
def calendar(stub_events):
    return Calendar(stub_events)


def test_events_getter(calendar):
    assert calendar.events == 'You have 2 events in four upcoming weeks.'


def test_new_event_invalid_type_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        event = 'New event of wrong type'
        calendar = Calendar()
        calendar.events = event
        assert 'should be of type Event, Workshop or Reminder' in excinfo.value


def test_add_new_event_positive(calendar, stub_event):
    calendar.events = stub_event
    assert calendar.events == 'You have 3 events in four upcoming weeks.'


def test_filter_by_date_with_existing_dates(calendar, stub_events):
    filtered_events = calendar.filter_by_date(
        start_date=datetime.now().replace(microsecond=0) + timedelta(days=3),
        end_date=datetime.now().replace(microsecond=0) + timedelta(days=5))
    assert filtered_events == [stub_events[0], stub_events[2]]


def test_filter_by_date_with_non_existing_start_date(calendar, stub_events):
    filtered_events = calendar.filter_by_date(start_date=datetime.now().replace(microsecond=0) + timedelta(weeks=7))
    assert filtered_events == []


def test_filter_by_date_without_params(calendar, stub_events):
    filtered_events = calendar.filter_by_date()
    assert filtered_events == [stub_events[0], stub_events[1], stub_events[2], stub_events[3]]


def test_filter_by_duration_without_params(calendar, stub_events):
    filtered_events = calendar.filter_by_duration()
    assert filtered_events == [stub_events[0], stub_events[1], stub_events[2], stub_events[3]]


def test_filter_by_duration_with_duration_min_param(calendar, stub_events):
    filtered_events = calendar.filter_by_duration(duration_min=30)
    assert filtered_events == [stub_events[1], stub_events[2], stub_events[3]]


def test_filter_by_duration_with_duration_max_param(calendar, stub_events):
    filtered_events = calendar.filter_by_duration(duration_max=30)
    assert filtered_events == [stub_events[0], stub_events[1]]


def test_filter_by_duration_with_duration_min_and_duration_max_params(calendar, stub_events):
    filtered_events = calendar.filter_by_duration(duration_min=30, duration_max=45)
    assert filtered_events == [stub_events[1], stub_events[3]]


def test_filter_by_duration_with_duration_param(calendar, stub_events):
    filtered_events = calendar.filter_by_duration(duration=50)
    assert filtered_events == [stub_events[2]]


def test_filter_with_duration_option_with_min_and_max_params(calendar, stub_events):
    filtered_events = calendar.filter('duration', min=28, max=47)
    assert filtered_events == [stub_events[1], stub_events[3]]


def test_filter_with_duration_option_and_min_param(calendar, stub_events):
    filtered_events = calendar.filter('duration', min=28)
    assert filtered_events == [stub_events[2], stub_events[1], stub_events[3]]


def test_filter_with_duration_option_and_max_param(calendar, stub_events):
    filtered_events = calendar.filter('duration', max=31)
    assert filtered_events == [stub_events[0], stub_events[1]]


def test_filter_with_duration_option_and_no_params(calendar, stub_events):
    filtered_events = calendar.filter('duration')
    assert filtered_events == [stub_events[0], stub_events[2], stub_events[1], stub_events[3]]


def test_filter_with_no_params(calendar, stub_events):
    filtered_events = calendar.filter()
    assert filtered_events == [stub_events[0], stub_events[2], stub_events[1], stub_events[3]]


def test_filter_with_title_option_and_no_params(calendar, stub_events):
    filtered_events = calendar.filter('title')
    assert filtered_events == [stub_events[0], stub_events[2], stub_events[1], stub_events[3]]


def test_filter_with_title_option_and_full_search_text(calendar, stub_events):
    filtered_events = calendar.filter('title', search_text='event 1')
    assert filtered_events == [stub_events[0]]


def test_filter_with_title_option_and_partial_search_text(calendar, stub_events):
    filtered_events = calendar.filter('title', search_text='ev')
    assert filtered_events == [stub_events[0], stub_events[1], stub_events[3]]


def test_filter_with_description_option_and_no_params(calendar, stub_events):
    filtered_events = calendar.filter('description')
    assert filtered_events == [stub_events[0], stub_events[2], stub_events[1], stub_events[3]]


def test_filter_with_description_option_and_full_search_text_param(calendar, stub_events):
    filtered_events = calendar.filter('description', search_text='Meet with John')
    assert filtered_events == [stub_events[2]]


def test_filter_with_description_option_and_partial_search_text_param(calendar, stub_events):
    filtered_events = calendar.filter('description', search_text='Another')
    assert filtered_events == [stub_events[1]]
