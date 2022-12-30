from datetime import datetime, timedelta

import pytest

from event import Event


@pytest.fixture
def event():
    return Event(1, datetime.now().replace(microsecond=0) + timedelta(hours=3), 20, '', '', '')


def test_duration_less_than_ten_minutes_raise_value_error():
    with pytest.raises(ValueError) as excinfo:
        e = Event(1, datetime.now() + timedelta(3), 5, '', '', '')

        assert 'can not be shorter than 10 minutes' in str(excinfo.value)


def test_duration_change_to_less_than_ten_minutes_raise_value_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.duration = 5

        assert 'can not be shorter than 10 minutes' in str(excinfo.value)


def test_duration_positive(event):
    assert event.duration == 20


def test_duration_invalid_type_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        e = Event(1, datetime.now() + timedelta(3), '5', '', '', '')

        assert 'Duration should be a positive digit.' in str(excinfo.value)


def test_start_date_with_less_than_hour_raise_value_error():
    with pytest.raises(ValueError) as excinfo:
        e = Event(1, datetime.now() + timedelta(minutes=45), 20, '', '', '')
        assert 'should not start in less than one hour' in excinfo.value


def test_start_date_change_with_less_than_hour_raise_value_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.start_date = datetime.now() + timedelta(minutes=45)

        assert 'should not start in less than one hour' in excinfo.value


def test_start_date_invalid_type_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        e = Event(1, 5, 30, '', '', '')

        assert 'Provided value is not date or time.' in str(excinfo.value)


def test_start_date_positive(event):
    assert f'{event.start_date:%A %b %y, %H:%M}' == f'{datetime.now() + timedelta(hours=3):%A %b %y, %H:%M}'


def test_dunder_str_of_class_event(event):
    assert f'{event!s}' == f', {datetime.now() + timedelta(hours=3):%A %b %y, %H:%M},' \
                           f' {(datetime.now() + timedelta(hours=3, minutes=20)):%A %b %y, %H:%M}'


def test_dunder_repr_of_class_event(event):
    assert f'{event!r}' == f"Event(idx=1, owner='', description='', title=''," \
                           f" duration=20, start_date={datetime.now().replace(microsecond=0) + timedelta(hours=3)!r})"
