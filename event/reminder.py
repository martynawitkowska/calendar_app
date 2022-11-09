from event import Event


class Reminder(Event):
    def __init__(self, start_date, duration, title, description, owner, remind):
        super().__init__(start_date, duration, title, description, owner)
        self.remind = remind
