from datetime import datetime, timedelta

import pytest

from calendar_2 import Calendar


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


def test_filter_with_owner_option_and_no_params(calendar, stub_events):
    filtered_events = calendar.filter('owner')
    assert filtered_events == [stub_events[0], stub_events[2], stub_events[1], stub_events[3]]


def test_filter_with_owner_option_and_full_search_name_param(calendar, stub_events):
    filtered_events = calendar.filter('owner', search_name='John')
    assert filtered_events == [stub_events[0], stub_events[1]]


def test_filter_with_owner_option_and_partial_search_name_param(calendar, stub_events):
    filtered_events = calendar.filter('owner', search_name='ry')
    assert filtered_events == [stub_events[2], stub_events[3]]


def test_filter_with_participants_option_and_no_params(stub_workshops):
    calendar = Calendar(stub_workshops)
    filtered_workshops = calendar.filter('participants')
    assert filtered_workshops == []


def test_filter_with_participants_option_and_full_search_name_param(stub_workshops):
    calendar = Calendar(stub_workshops)
    filtered_workshops = calendar.filter('participants', search_name='Mary')
    assert filtered_workshops == [stub_workshops[0]]


def test_filter_with_participants_option_and_partial_search_name_param(stub_workshops):
    calendar = Calendar(stub_workshops)
    filtered_workshops = calendar.filter('participants', search_name='mily')
    assert filtered_workshops == []


@pytest.mark.xfail(raises=ValueError)
def test_remove_raise_value_error_xfail(calendar):
    assert calendar.remove(5)


def test_remove_raise_value_error_pytest_raises(calendar):
    with pytest.raises(ValueError) as excinfo:
        calendar.remove(5)
        assert 'Provided idx: 5 does not appear to exist in this calendar' in excinfo.value


def test_remove_positive(calendar, stub_events):
    calendar.remove(2)
    get_events = calendar.filter('duration')
    assert get_events == [stub_events[0], stub_events[1], stub_events[2]]


def test_dunder_len_negative(calendar):
    assert not (len(calendar) == 5)


def test_dunder_len_positive(calendar):
    assert len(calendar) == 4
