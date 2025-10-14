from datetime import date
import datetime
from uuid import UUID


class Task:
    _id:UUID
    _title:str
    _description:str 
    _created_at:date 
    _due_date: date
    _completed_at: date
    _status: str
    _priority:int
    _tags:str

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
        

        self._id = id or UUID()
        self._title = title
        self._description = description
        self._created_at = created_at or datetime.now()
        self._due_date = due_date
        self._completed_at = completed_at
        self._status = status
        self._priority = priority
        self._tags = tags

    
    @property
    def id(self) ->  UUID:
        return self._id
    
    @property 
    def title(self) -> str:
        return self._title
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def created_at(self) -> date:
        return self._completed_at
    
    @property
    def due_date(self) -> date:
        return self._due_date
    
    @property
    def completed_at(self) -> date:
        return self._completed_at
    
    @property
    def status(self) -> str:
        return self._status
    
    @property
    def priority(self) -> int:
        return self._priority
    
    @property
    def tags(self) -> str:
        return self._tags