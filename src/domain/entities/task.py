
from datetime import date
from uuid import uuid4

class Task:
    id: str
    title: str | None
    description: str | None
    created_at: date
    due_date: date | None
    completed_at: date | None
    status: str | None
    priority: int | None
    tags: str | None

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id") or uuid4().hex
        self.title = kwargs.get("title")
        self.description = kwargs.get("description")
        self.created_at =  kwargs.get("created_at")  or date.today()
        self.due_date = kwargs.get("due_date")
        self.completed_at = kwargs.get("completed_at")
        self.status = kwargs.get("status")
        self.priority = kwargs.get("priority")
        self.tags = kwargs.get("tags")
        