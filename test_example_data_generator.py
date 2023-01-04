import datetime

from example_data_generator import event_data


def test_event_data_generator_object_beginning_date_attribute():
    assert event_data.beginning_date == datetime.date.today() + datetime.timedelta(days=12)


def test_event_data_generator_object_durations_attribute():
    assert event_data.durations == (15, 180)


def test_event_data_generator_object_titles_attribute():
    assert event_data.titles == ['lunch', 'lecture', 'ceo meeting', 'seminar', 'sport event']


def test_event_data_generator_object_descriptions_attribute():
    assert event_data.descriptions == ['nice event', 'some meeting', 'emergency meeting', 'be happy', 'do not be sad']


def test_event_data_generator_object_users_attribute():
    assert event_data.users == ['Mister Someone', 'Zdzisiek', 'Wojtek', 'Happy Person', 'Another Person']


def test_event_data_generator_object_reminder_attribute():
    assert not event_data.reminder


def test_event_data_generator_object_workshop_attribute():
    assert not event_data.workshop

