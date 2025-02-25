from typing import List, Any

from pos.core.models.campaigns import DiscountItem, DiscountPrice, BuyNGetN, Combo
from pos.core.models.repositories import CampaignRepository
from pos.infra.database import Database


class CampaignSQLiteRepository(CampaignRepository):
    def __init__(self, db: Database):
        self.db = db

    def create_discount_item(self, campaign: DiscountItem) -> DiscountItem:
        self.db.execute("INSERT INTO discount_items (id, product_id, discount) VALUES (?, ?, ?)",
                        (campaign.id, campaign.product_id, campaign.discount))
        return campaign

    def create_discount_price(self, campaign: DiscountPrice) -> DiscountPrice:
        self.db.execute("INSERT INTO discount_prices (id, price, discount) VALUES (?, ?, ?)",
                        (campaign.id, campaign.price, campaign.discount))
        return campaign

    def create_buy_n_get_n(self, campaign: BuyNGetN) -> BuyNGetN:
        self.db.execute("INSERT INTO buyNgetN (id, product_id, product_amount, gift_id, gift_amount) "
                        "VALUES (?, ?, ?, ?, ?)",
                        (campaign.id,campaign.product_id,campaign.product_amount,
                         campaign.gift_id,campaign.gift_amount))
        return campaign

    def create_combo(self, campaign: Combo) -> Combo:
        self.db.execute("INSERT INTO combo (id, products_id, discount) VALUES (?, ?, ?)",
                        (campaign.id, campaign.products, campaign.discount))
        return campaign

    def delete(self, campaign_id: str) -> None:
        self.db.execute("DELETE FROM discount_items WHERE id = ?", (campaign_id,))
        self.db.execute("DELETE FROM discount_price WHERE id = ?", (campaign_id,))
        self.db.execute("DELETE FROM buyNgetN WHERE id = ?", (campaign_id,))
        self.db.execute("DELETE FROM combo WHERE id = ?", (campaign_id,))

    def list(self) -> List[Any]:
        campaigns = []

        discount_items = self.db.fetchall("SELECT * FROM discount_items")

        if discount_items:
            for campaign in discount_items:
                campaigns.append(DiscountItem(id=campaign[0], product_id=campaign[1],discount=campaign[2]))

        discount_prices = self.db.fetchall("SELECT * FROM discount_price")

        if discount_prices:
            for campaign in discount_prices:
                campaigns.append(DiscountPrice(id=campaign[0], price=campaign[1], discount=campaign[2]))

        but_n_get_n = self.db.fetchall("SELECT * FROM buyNgetN")

        if but_n_get_n:
            for campaign in but_n_get_n:
                campaigns.append(BuyNGetN(id=campaign[0], product_id=campaign[1], product_amount=campaign[2]
                                          , gift_id=campaign[3], gift_amount=campaign[4]))

        combos = self.db.fetchall("SELECT * FROM combo")

        if combos:
            for campaign in combos:
                campaigns.append(Combo(id=campaign[0], products=campaign[1], discount=campaign[2]))

        return campaigns



