from abc import ABC, abstractmethod

from src.domain.adapters.dto import DtoTask
from src.domain.adapters.repository import IRepository
from src.domain.entities.task import Task


class IFactoryTask(ABC):
    
    @abstractmethod
    def create_task(self, t:DtoTask) -> None:
        pass

    @abstractmethod
    def delete_task(self, id:str) -> None:
        pass

    @abstractmethod
    def get_task(self, id:str) -> Task:
        pass

    @abstractmethod
    def get_tasks(self) -> dict:
        pass

    @abstractmethod
    def update_task(self, t:DtoTask) -> None:
        pass