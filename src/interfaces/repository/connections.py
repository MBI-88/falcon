from sqlite3 import Connection
from typing import override
from uuid import UUID
from src.domain.adapters.repository import IRepository
from src.domain.entities.task import Task




class DbConnections(IRepository):

    def __init__(self, conn: Connection) -> None:
        self._conn = conn
    
    @override
    def save(self, t: Task) -> None:
        self._conn.execute("""
                INSERT INTO tasks (id, title, description, created_at, due_date, completed_at, status, priority, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (t.title, t.description, t.created_at, t.due_date,
                  t.completed_at, t.status, t.priority, t.tags))
        self._conn.commit()
    
    @override
    def update(self, t: Task) -> None:
        self._conn.execute("""
                UPDATE tasks
                SET title=?, description=?, due_date=?, completed_at=?, status=?, priority=?, tags=?
                WHERE id=?
            """, (t.title, t.description, t.due_date, t.completed_at,
                  t.status, t.priority, t.tags, t.id))
        self._conn.commit()

    @override
    def delete(self, id:UUID) -> None:
        self._conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self._conn.commit()
    

    @override
    def all(self) -> dict:
        rows = self._conn.execute("SELECT * FROM tasks ORDER BY created_at DESC").fetchall()
        return {
            "tasks": [dict(row) for row in rows],
        }

    @override
    def find(self, id: UUID) -> dict:
        row = self._conn.execute("SELECT * FROM tasks WHERE id = ?", (id,)).fetchone()
        return {
            **dict(row)
        }
    
    

def NewDbConnection(conn: Connection) -> IRepository: 
    return DbConnections(conn=conn)