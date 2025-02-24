import sqlite3

class Database:
    def __init__(self, db_path="pos.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        pass

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()