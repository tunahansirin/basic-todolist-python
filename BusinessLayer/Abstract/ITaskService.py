from abc import ABC, abstractmethod
from typing import List, Optional
from BusinessLayer.Abstract.IGenericService import IGenericService
from EntityLayer.Concrete.Task import Task

# ITaskService interface'i IGenericService interface'inden miras alır.
# ITaskService sınıfı kendi metodları da bulunmaktadır.

class ITaskService(IGenericService[Task], ABC):
    
    @abstractmethod
    def GetAllByUserID(self, userID: int) -> List[Task]:
        pass

    @abstractmethod
    def AddRange(self, tasks: List[Task]) -> None:
        pass

    @abstractmethod
    def GetAllTasksByListID(self, taskListID: int) -> List[Task]:
        pass

    @abstractmethod
    def GetCompletedTasksByListID(self, taskListID: int) -> List[Task]:
        pass

    @abstractmethod
    def GetIncompleteTasksByListID(self, taskListID: int) -> List[Task]:
        pass

    @abstractmethod
    def UpdateTaskStatus(self, taskListId: int, status: int) -> None:
        pass
