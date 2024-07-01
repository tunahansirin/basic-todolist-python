from abc import ABC, abstractmethod
from typing import List
from BusinessLayer.Abstract.IGenericService import IGenericService
from EntityLayer.Concrete.TaskList import TaskList

# ITaskListService interface'i IGenericService interface'inden miras alır.
# ITaskListService sınıfı kendi metodları da bulunmaktadır.

class ITaskListService(IGenericService[TaskList], ABC):
    
    @abstractmethod
    def GetAllByUserIDOrderByDate(self, userID: int) -> List[TaskList]:
        pass

    @abstractmethod
    def GetAllByUserIDOrderByNameAsc(self, userID: int) -> List[TaskList]:
        pass

    @abstractmethod
    def GetAllByUserIDOrderByNameDesc(self, userID: int) -> List[TaskList]:
        pass