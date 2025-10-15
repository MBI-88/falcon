from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.adapters.dto import DtoTask
from src.domain.adapters.repository import IRepository
from src.domain.entities.task import Task


class IFactoryTask(ABC):
    
    @abstractmethod
    def create_task(self, t:DtoTask) -> None:
        pass

    @abstractmethod
    def delete_task(self, id:int) -> None:
        pass

    @abstractmethod
    def get_task(self, id:int) -> Task:
        pass

    @abstractmethod
    def get_tasks(self) -> dict:
        pass

    @abstractmethod
    def update_task(self, t:DtoTask) -> None:
        pass