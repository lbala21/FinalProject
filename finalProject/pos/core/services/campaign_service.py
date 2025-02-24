from typing import Any, List

from pos.core.models.campaigns import BuyNGetN, Combo, DiscountItem, DiscountPrice
from pos.core.models.repositories import CampaignRepository


class ReportService:
    def __init__(self, campaign_repository: CampaignRepository):
        self.campaign_repository = campaign_repository

    def create_discount_item_campaign(
        self, product_id: str, discount: int
    ) -> DiscountItem:
        pass

    def create_discount_price_campaign(
        self, price: int, discount: int
    ) -> DiscountPrice:
        pass

    def create_buy_n_get_n_campaign(
        self, product_id: str, product_amount: int, gift_id: str, gift_amount: int
    ) -> BuyNGetN:
        pass

    def create_combo_campaign(self, products: List[str], discount: int) -> Combo:
        pass

    def delete_discount_campaign(self, campaign_id: str) -> None:
        pass

    def list_campaigns(self) -> List[Any]:
        pass
