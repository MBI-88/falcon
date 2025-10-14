from typing import override
from uuid import UUID

from src.domain.adapters.dto import DtoTask
from src.domain.adapters.repository import IRepository
from src.domain.entities.task import Task
from src.interactors.task.interface import IFactoryTask



class FactoryTask(IFactoryTask):

    def __init__(self, repo:IRepository) -> None:
        self._repo = repo
    
    @override
    def create_task(self, t: DtoTask) -> None:
        try:
            task = Task(**t.get_dto)
            self._repo.save(task)
        except:
            raise ValueError("Database error")
            

    @override
    def update_task(self, t:DtoTask) -> None:
        try:
            task = Task(**t.get_dto)
            self._repo.update(task)
        except:
            raise ValueError("Database error")
        
    
    @override
    def delete_task(self, id: UUID) -> None:
        try:
            self._repo.delete(id)
        except:
            raise ValueError("Database error")
    
    @override
    def get_task(self, id: UUID) -> Task:
        try:
            task = self._repo.find(id)
            return Task(**task)
        except:
            raise ValueError("Database error")
    
    @override
    def get_tasks(self) -> dict:
        try:
            return self._repo.all()
        except:
            raise ValueError("Database error")




def NewFactoryTask(repo:IRepository) -> IFactoryTask:
    return FactoryTask(repo)