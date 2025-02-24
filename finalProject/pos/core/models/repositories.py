from typing import TypeVar, Protocol, Optional

ItemT = TypeVar("ItemT")

class Repository(Protocol[ItemT]):
    def create(self, item: ItemT) -> ItemT:
        pass

    def read(self, item_id: int) -> Optional[ItemT]:
        pass

    def update(self, item: ItemT) -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass