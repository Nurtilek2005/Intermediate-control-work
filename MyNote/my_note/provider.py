import abc
import csv
import json
from abc import ABC

from my_note.note import Note


class Provider(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def add(self, note: Note):
        pass

    @abc.abstractmethod
    def write(self, data):
        pass

    @abc.abstractmethod
    def save(self):
        pass


class CsvProvider(Provider):
    filename = "data.csv"
    fieldnames = ["name", "body"]

    def __init__(self):
        super().__init__("CSV провайдер")
        try:
            file = open(self.filename, "r", encoding="UTF-8")
            file.close()
        except FileNotFoundError:
            self.init_file()
        except PermissionError:
            print(f"Файл {self.filename} не читабельный!")
            exit()

    def init_file(self):
        file = open(self.filename, "w", newline="", encoding="UTF-8")
        writer = csv.DictWriter(file, fieldnames=self.fieldnames, delimiter=";")
        writer.writeheader()
        file.close()

    def read(self):
        try:
            file = open(self.filename, "r", newline="", encoding="UTF-8")
            reader = csv.DictReader(file, delimiter=";")
            data: list[dict] = list()
            for row in reader:
                row: dict = row
                data.append(row)
            file.close()
            return data
        except FileNotFoundError:
            self.init_file()
            return self.read()
        except PermissionError:
            print(f"Файл {self.filename} не читабельный!")
            exit()

    def add(self, note: Note):
        pass

    def write(self, data):
        pass

    def save(self):
        pass


class JsonProvider(Provider, ABC):
    filename = "data.json"

    def __init__(self):
        super().__init__("JSON провайдер")
        try:
            file = open(self.filename, "r", encoding="UTF-8")
            file.close()
        except FileNotFoundError:
            self.init_file()
        except PermissionError:
            print(f"Файл {self.filename} не читабельный!")
            exit()

    def init_file(self):
        file = open(self.filename, "w", encoding="UTF-8")
        json.dump([], file, indent=4)
        file.close()

    def read(self):
        try:
            file = open(self.filename, "r", encoding="UTF-8")
            data = json.load(file)
            file.close()
            return data
        except FileNotFoundError:
            self.init_file()
            return self.read()
        except PermissionError:
            print(f"Файл {self.filename} не читабельный!")
            exit()

    def add(self, note: Note):
        pass

    def write(self, data):
        pass

    def save(self):
        pass
