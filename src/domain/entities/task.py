
from datetime import date
from uuid import uuid4

class Task:
    id: str
    title: str
    description: str
    created_at: date
    due_date: date
    completed_at: date
    status: str
    priority: int
    tags: str

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id") or uuid4().hex
        self.title = kwargs.get("title") or ""
        self.description = kwargs.get("description") or ""
        self.created_at =  kwargs.get("created_at")  or date.today()
        self.due_date = kwargs.get("due_date") or date.today()
        self.completed_at = kwargs.get("completed_at") or date.today()
        self.status = kwargs.get("status") or "pending"
        self.priority = kwargs.get("priority") or 1
        self.tags = kwargs.get("tags") or "normal"
        