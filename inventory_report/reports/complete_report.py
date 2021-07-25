from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)

        company = [item["nome_da_empresa"] for item in list]

        products_by_company = ""
        total = Counter(company)
        for company_name in total:
            products_by_company += f"- {company_name}: {total[company_name]}\n"

        complete_report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{products_by_company}"
        )

        return complete_report
