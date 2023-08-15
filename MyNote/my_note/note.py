from datetime import datetime


class Note(object):
    name: str
    body: str
    datetime: datetime

    def __init__(self, name: str, body: str):
        self.name = name
        self.body = body
        self.datetime = datetime.now()

    def get_name(self):
        return self.name

    def get_body(self):
        return self.body

    def get_datetime(self):
        return self.datetime
