import datetime

from data_generator import DataGenerator

event_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=12),
    (15, 180),
    ['lunch', 'lecture', 'ceo meeting', 'seminar', 'sport event'],
    ['nice event', 'some meeting', 'emergency meeting', 'be happy', 'do not be sad'],
    ['Mister Someone', 'Zdzisiek', 'Wojtek', 'Happy Person', 'Another Person'],
    False,
    False
)

events = event_data.generate_data(150)
event_data.save_data(events, 'event_data.json')

reminder_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=12),
    (15, 180),
    ['lunch', 'lecture', 'ceo meeting', 'seminar', 'sport event'],
    ['nice event', 'some meeting', 'emergency meeting', 'be happy', 'do not be sad'],
    ['Mister Someone', 'Zdzisiek', 'Wojtek', 'Happy Person', 'Another Person'],
    True,
    False
)

reminders = reminder_data.generate_data(50)
reminder_data.save_data(reminders, 'reminder_data.json')

workshop_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=12),
    (15, 180),
    ['lunch', 'lecture', 'ceo meeting', 'seminar', 'sport event'],
    ['nice event', 'some meeting', 'emergency meeting', 'be happy', 'do not be sad'],
    ['Mister Someone', 'Zdzisiek', 'Wojtek', 'Happy Person', 'Another Person'],
    False,
    True
)

workshops = workshop_data.generate_data(50)
workshop_data.save_data(workshops, 'workshop_data.json')
