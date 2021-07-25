import os
from json import load
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        _, file_extension = os.path.splitext(path)

        if file_extension == ".json":
            return cls.open_file(path)
        else:
            raise ValueError("File must be a valid JSON format.")

    @classmethod
    def open_file(cls, path):
        with open(path) as file:
            data = load(file)
            return list(data)
