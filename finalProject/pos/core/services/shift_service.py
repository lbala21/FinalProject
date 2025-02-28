from pos.core.models.repositories import ShiftRepository
from pos.core.models.shift import Shift


class ShiftService:
    def __init__(self, shift_repo: ShiftRepository):
        self.shift_repo = shift_repo

    def create_shift(self, shift_id: str, cashier: str) -> Shift:
        pass

    def read_shift(self, shift_id: str) -> Shift:
        pass

    def close_shift(self, shift_id:str) -> None:
        pass