from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.task import Task

class IRepository(ABC):

    @abstractmethod
    def save(self, t:Task) -> None:
        pass
        
    @abstractmethod    
    def update(self, t:Task) -> None:
        pass
    

    @abstractmethod
    def delete(self, id:str) -> None: 
        pass

    @abstractmethod
    def all(self) -> dict:
        pass

    @abstractmethod
    def find(self, id:str) -> dict:
        pass