from datetime import timedelta, datetime

from event import Workshop


def test_create_workshop_instance():
    workshop = Workshop(1, datetime.now() + timedelta(hours=3), 20, '', '', '', ['', '', ''])

    assert workshop.participants == ['', '', '']
