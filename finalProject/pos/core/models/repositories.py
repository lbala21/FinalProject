from typing import Optional, Protocol, TypeVar

ItemT = TypeVar("ItemT")


class CampaignRepository(Protocol[ItemT]):
    def create(self, item: ItemT) -> ItemT:
        pass

    def read(self, item_id: int) -> Optional[ItemT]:
        pass

    def update(self, item: ItemT) -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass


class ReportRepository(Protocol[ItemT]):
    def create(self, item: ItemT) -> ItemT:
        pass

    def read(self, item_id: int) -> Optional[ItemT]:
        pass

    def update(self, item: ItemT) -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass


class ReceiptRepository(Protocol[ItemT]):
    def create(self, item: ItemT) -> ItemT:
        pass

    def read(self, item_id: int) -> Optional[ItemT]:
        pass

    def update(self, item: ItemT) -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass


class ProductRepository(Protocol[ItemT]):
    def create(self, item: ItemT) -> ItemT:
        pass

    def read(self, item_id: int) -> Optional[ItemT]:
        pass

    def update(self, item: ItemT) -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass


class SalesRepository(Protocol[ItemT]):
    def create(self, item: ItemT) -> ItemT:
        pass

    def read(self, item_id: int) -> Optional[ItemT]:
        pass

    def update(self, item: ItemT) -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass
