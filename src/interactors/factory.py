from datetime import date
from typing import override

from src.domain.adapters.dto import DtoTask
from src.domain.adapters.repository import IRepository
from src.domain.entities.task import Task
from src.interactors.interface import IFactoryTask



class FactoryTask(IFactoryTask):

    def __init__(self, repo:IRepository) -> None:
        self._repo = repo
    
    @override
    def create_task(self, t: DtoTask) -> None:
        try:
            body = self.check_data(t.get_dto)
            task = Task(**body)
            self._repo.save(task)
        except ValueError as e:
            raise e
            

    @override
    def update_task(self, t:DtoTask) -> None:
        try:
            body = self.check_data(t.get_dto)
            task = Task(**body)
            self._repo.update(task)
        except ValueError as e:
            raise e
        
    
    @override
    def delete_task(self, id: str) -> None:
        try:
            self._repo.delete(id)
        except ValueError as e:
            raise e
    
    @override
    def get_task(self, id: str) -> Task:
        try:
            task = self._repo.find(id)
            return Task(**task)
        except ValueError as e:
            raise e
    
    @override
    def get_tasks(self) -> dict:
        try:
            return self._repo.all()
        except ValueError as e:
            raise e


    def check_data(self, data: dict) -> dict:
        body = {}
        for key, value in data.items():
            if value in (None, ""):
                continue

            match key:
                case "created_at" | "due_date" | "completed_at":
                    try:
                        body[key] = date.fromisoformat(value)
                    except ValueError:
                        raise ValueError(f"Invalid format date '{key}': {value}")
                case _:
                    body[key] = value
        return body



def NewFactoryTask(repo:IRepository) -> IFactoryTask:
    return FactoryTask(repo)