from pos.core.models.repositories import ShiftRepository
from pos.core.models.shift import Shift
from pos.infra.database import Database


class ShiftSQLiteRepository(ShiftRepository):
    def __init__(self, db: Database):
        self.db = db

    def create(self, shift: Shift) -> Shift:
        self.db.execute("INSERT INTO shifts (id, cashier, is_open) "
                        "VALUE(?,?,?)",
                        (shift.id, shift.cashier, shift.is_open))
        return shift

    def close(self, shift_id: str) -> None:
        self.db.execute("DELETE FROM shifts WHERE id = ?",
                        (shift_id,))

