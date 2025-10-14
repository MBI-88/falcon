from sqlite3 import Connection
from uuid import UUID

from domain.entities.task import Task




class DbConnections:

    def __init__(self, conn: Connection) -> None:
        self._conn = conn
    

    def save(self, t: Task) -> None:
        self._conn.execute("""
                INSERT INTO tasks (id, title, description, created_at, due_date, completed_at, status, priority, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (t.title, t.description, t.created_at, t.due_date,
                  t.completed_at, t.status, t.priority, t.tags))
        self._conn.commit()
    

    def update(self, t: Task) -> None:
        self._conn.execute("""
                UPDATE tasks
                SET title=?, description=?, due_date=?, completed_at=?, status=?, priority=?, tags=?
                WHERE id=?
            """, (t.title, t.description, t.due_date, t.completed_at,
                  t.status, t.priority, t.tags, t.id))
        self._conn.commit()
    
    def delete(self, id:UUID) -> None:
        self._conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self._conn.commit()
    
    