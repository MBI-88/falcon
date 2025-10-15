from dataclasses import dataclass
from datetime import date
import datetime
from uuid import UUID

@dataclass
class Task:
    ID: UUID
    Title: str
    Description: str
    Created_at: date
    Due_date: date
    Completed_at: date
    Status: str
    Priority: int
    Tags: str

    def __init__(self, 
                 id:UUID,
                 title:str, 
                 description:str, 
                 created_at:date, 
                 due_date: date,
                 completed_at: date,
                 status: str,
                 priority:int,
                 tags:str
                ) -> None:
        

        self.ID = id or UUID()
        self.Title = title
        self.Description = description
        self.Created_at = created_at or datetime.now()
        self.Due_date = due_date
        self.Completed_at = completed_at
        self.Status = status
        self.Priority = priority
        self.Tags = tags

    
    @property
    def id(self) ->  UUID:
        return self.ID
    
    @property 
    def title(self) -> str:
        return self.Title
    
    @property
    def description(self) -> str:
        return self.Description
    
    @property
    def created_at(self) -> date:
        return self.Created_at
    
    @property
    def due_date(self) -> date:
        return self.Due_date
    
    @property
    def completed_at(self) -> date:
        return self.Completed_at
    
    @property
    def status(self) -> str:
        return self.Status
    
    @property
    def priority(self) -> int:
        return self.Priority
    
    @property
    def tags(self) -> str:
        return self.Tags