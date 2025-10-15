class DtoTask:

    def __init__(self, 
                 id:str | None,
                 title:str | None, 
                 description:str | None, 
                 created_at:str | None, 
                 due_date: str | None,
                 completed_at: str | None,
                 status: str | None,
                 priority:int | None,
                 tags:str | None
                 ) -> None:
       

        self._dto = {
            "id": id,
            "title": title,
            "description": description,
            "created_at": created_at,
            "due_date": due_date,
            "completed_at": completed_at,
            "status": status,
            "priority": priority,
            "tags": tags,
        }
        
    
    
    @property
    def get_dto(self) -> dict:
        return self._dto