from typing import Protocol

from pos.core.models.repositories import (CampaignRepository, ReportRepository, ReceiptRepository, ProductRepository, SalesRepository)


class _Infra(Protocol):

    def product_repo(self) -> ProductRepository:
        pass

    def receipt_repo(self) -> ReceiptRepository:
        pass

    def sales_repo(self) -> SalesRepository:
       pass

    def campaign_repo(self) -> CampaignRepository:
        pass

    def report_repo(self) -> ReportRepository:
        pass

