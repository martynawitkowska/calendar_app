import io
from datetime import timedelta, date
from unittest.mock import Mock, patch

import pytest

from data_generator import DataGenerator


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
def generated_data(data_generator_workshop_false):
    return data_generator_workshop_false.generate_data(2)



def test_create_data_generator_object():
    generate_data = DataGenerator(date.today() + timedelta(days=12),
                                  (15, 180),
                                  ['lunch', 'lecture'],
                                  ['nice event', 'some meeting'],
                                  ['Mister Someone', 'John'],
                                  True,
                                  False)

    assert generate_data.durations == (15, 180)
    assert generate_data.titles == ['lunch', 'lecture']
    assert generate_data.descriptions == ['nice event', 'some meeting']
    assert generate_data.users == ['Mister Someone', 'John']


def test_generate_data_workshop_false(data_generator_workshop_false):
    generated_data = data_generator_workshop_false.generate_data(2)
    assert len(generated_data) == 2
    for idx in range(len(generated_data)):
        assert generated_data[idx].get('idx') == idx


def test_generate_data_workshop_true(data_generator_workshop_true):
    generated_data = data_generator_workshop_true.generate_data(3)
    for idx in range(len(generated_data)):
        assert generated_data[idx].get('idx') == idx


def test_save_data(tmp_path):
    path = tmp_path / 'test_file.json'
    data = [{'some key': 'A lot data to save'}]
    DataGenerator.save_data(data, str(path))
    assert path.read_text() == '[{"some key": "A lot data to save"}]'


def test_load_data(tmp_path):
    json_file = '[{"some key": "some value"}, {"some other key": "some other value"}]'
    path = tmp_path / 'test_file.json'
    path.write_text(json_file)
    loaded_data = DataGenerator.load_data(path)
    assert loaded_data[0] == {'some key': 'some value'}
    assert loaded_data[1] == {'some other key': 'some other value'}

