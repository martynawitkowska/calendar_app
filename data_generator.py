import datetime
import random
from pprint  import pprint as pp


class DataGenerator:
    def __init__(self, beginning_date, durations, titles, descriptions, users, reminder=False, workshop=False):
        self.beginning_date = beginning_date
        self.durations = durations
        self.titles = titles
        self.descriptions = descriptions
        self.users = users
        self.reminder = reminder
        self.workshop = workshop

    def generate_data(self, amount):
        events = []

        for idx in range(amount):
            event = {
                'idx': idx,
                'start_date': self.beginning_date + datetime.timedelta(hours=random.randint(1, 5000)),
                'duration': random.randint(*self.durations),
                'title': random.choice(self.titles),
                'description': random.choice(self.descriptions),
                'owner': random.choice(self.users)
            }

            if self.reminder:
                event['reminder'] = random.choice([True, False])

            if self.workshop:
                event['workshop'] = random.choices(self.users, k=random.randint(2, 20))

            events.append(event)

        pp(events)


d = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=12),
    (15, 180),
    ['lunch', 'lecture', 'ceo meeting', 'seminar', 'sport event'],
    ['nice event', 'some meeting', 'emergency meeting', 'be happy', 'do not be sad'],
    ['Mister Someone', 'Zdzisiek', 'Wojtek', 'Happy Person', 'Another Person'],
    False,
    True
)
d.generate_data(50)
