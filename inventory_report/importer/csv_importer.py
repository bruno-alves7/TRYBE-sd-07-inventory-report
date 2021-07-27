import os
from csv import DictReader
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        _, file_extension = os.path.splitext(path)

        if file_extension == ".csv":
            return cls.open_file(path)
        else:
            raise ValueError("Arquivo inválido")

    @classmethod
    def open_file(cls, path):
        with open(path) as file:
            data = DictReader(file)
            return list(data)
