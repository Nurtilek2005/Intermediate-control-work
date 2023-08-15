from my_note.note import Note
from my_note.provider import Provider, JsonProvider, CsvProvider


class Program:
    provider: Provider

    def __init__(self):
        self.__load_provider()

    def __load_provider(self):
        self.provider = JsonProvider()
        print(self.provider.read())

    def run(self):
        my_note = Note("test", "this a test note")


if __name__ == '__main__':
    program = Program()
    program.run()

