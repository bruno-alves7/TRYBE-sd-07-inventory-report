from datetime import datetime
from statistics import mode


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        today = datetime.today()
        today_formated = f"{today.year}-0{today.month}-{today.day}"

        oldest_fabrication_date = min(
            [
                datetime.strptime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for data in stock
            ]
        )

        closest_expiration_date = min(
            [
                datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
                for data in stock
                if datetime.strptime(
                    data["data_de_validade"], "%Y-%m-%d"
                ).date()
                > datetime.strptime(today_formated, "%Y-%m-%d").date()
            ]
        )

        stock = mode([data["nome_da_empresa"] for data in stock])

        report = (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        )

        return report
