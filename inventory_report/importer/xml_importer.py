import os
from xml.etree import ElementTree
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        _, file_extension = os.path.splitext(path)

        if file_extension == ".xml":
            return cls.open_file(path)
        else:
            raise ValueError("File must be a valid XML format.")

    @classmethod
    def open_file(cls, path):
        with open(path) as file:
            tree = ElementTree.parse(file)
            root = tree.getroot().findall("record")
            data = []

            for element in root:
                dictionary = {}

                for item in element:
                    dictionary[item.tag] = item.text

                data.append(dictionary)

            return data
