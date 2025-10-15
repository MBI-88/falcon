from datetime import date
import datetime
import sqlite3
from uuid import UUID

from config.config import DATABASE


class DbConfig:   
    def get_connection(self):
        try: 
            self._conn = sqlite3.connect(DATABASE)
            self._conn.row_factory = sqlite3.Row
            return self._conn
        except ValueError:
            raise ValueError("Database creation error")

    def create_table(self, sql:str):
        try:
            self._conn.execute(sql)
            self._conn.commit()
        except ValueError:
            raise ValueError("Create table error")