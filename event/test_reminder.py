from datetime import datetime, timedelta

from event import Reminder


def test_create_reminder_instance():
    reminder = Reminder(1, datetime.now() + timedelta(hours=3), 20, '', '', '', True)

    assert reminder.remind == True
