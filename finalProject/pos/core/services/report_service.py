from pos.core.models.report import Report
from pos.core.models.repositories import ReportRepository


class ReportService:
    def __init__(self, report_repository: ReportRepository):
        self.report_repo = report_repository

    def get_sales(self) -> Report:
        """Generate a report based on closed receipts."""
        sales = self.report_repo.generate()
        return sales
