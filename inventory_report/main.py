import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_path = sys.argv[1]
    ext = sys.argv[1].split(".")[-1]
    type = sys.argv[2]

    types = {
        "json": JsonImporter,
        "csv": CsvImporter,
        "xml": XmlImporter,
    }

    inventory = InventoryRefactor(types[ext])
    print(inventory.import_data(file_path, type), end="")
