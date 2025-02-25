import sqlite3
from typing import Any, List


class Database:
    def __init__(self, db_path: str = "pos.db") -> None:
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        self.cursor.executescript("""
        CREATE TABLE IF NOT EXISTS products (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS buyNgetN(
            id TEXT PRIMARY KEY,
            product_id TEXT NOT NULL,
            product_amount INTEGER NOT NULL,
            gift_id TEXT NOT NULL,
            gift_amount INTEGER NOT NULL,
            FOREIGN KEY(product_id, gift_id) REFERENCES products(id),
        );
        
        CREATE TABLE IF NOT EXISTS combo(
            id TEXT PRIMARY KEY,
            products_id TEXT NOT NULL, 
            discount INTEGER NOT NULL,
        );
        
        CREATE TABLE IF NOT EXISTS discount_items(
            id TEXT PRIMARY KEY,
            product_id TEXT NOT NULL,
            discount INTEGER NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(id),
        );
        
        CREATE TABLE IF NOT EXISTS discount_price(
            id TEXT PRIMARY KEY,
            price INTEGER NOT NULL,
            discount INTEGER NOT NULL,
        );
        
        CREATE TABLE IF NOT EXISTS receipts(
            id TEXT PRIMARY KEY,
            shift_id TEXT NOT NULL,
            is_open BOOLEAN,
            products TEXT,
            total_price INTEGER NOT NULL,
            FOREIGN KEY(shift_id) REFERENCES shifts(id),
        );
        
        CREATE TABLE IF NOT EXISTS shifts(
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            FOREIGN KEY(id) REFERENCES receipts(shift_id),
        )
        """)
        self.connection.commit()

    def execute(self, query: str, params: tuple[Any, ...] = ()) -> None:
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query: str, params: tuple[Any, ...] = ()) -> List[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query: str, params: tuple[Any, ...] = ()) -> Any:
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
