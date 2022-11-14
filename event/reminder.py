from event import Event


class Reminder(Event):
    def __init__(self, idx, start_date, duration, title, description, owner, remind):
        super().__init__(idx, start_date, duration, title, description, owner)
        self.remind = remind
