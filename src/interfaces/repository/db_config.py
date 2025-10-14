from datetime import date
import datetime
import sqlite3
from uuid import UUID

from config.config import DATABASE


class DbConfig:   
    def get_connection(self):
        self._conn = sqlite3.connect(DATABASE)
        self._conn.row_factory = sqlite3.Row
        return self._conn
    
    def python_type_to_sqlite(self, py_type):
        if py_type == str:
            return "TEXT"
        elif py_type == int:
            return "INTEGER"
        elif py_type == float:
            return "REAL"
        elif py_type in [date, datetime]:
            return "DATETIME"
        elif py_type == UUID:
            return "TEXT"
        else:
            return "TEXT"  # Fallback

    def create_table(self, cls):
        table_name = cls.__name__.lower() + "s"
        fields = cls.__annotations__

        columns = []
        for name, py_type in fields.items():
            sql_type = self.python_type_to_sqlite(py_type)
            column_def = f"{name} {sql_type}"
            if name == "ID":
                column_def += " PRIMARY KEY"
            columns.append(column_def)

        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n  " + ",\n  ".join(columns) + "\n);"
        self._conn.execute(sql)
        self._conn.commit()