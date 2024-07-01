from abc import ABC, abstractmethod
from typing import Optional
from BusinessLayer.Abstract.IGenericService import IGenericService
from EntityLayer.Concrete.User import User

# IUserService interface'i IGenericService interface'inden miras alır.
# IUserService sınıfı kendi metodları da bulunmaktadır.

class IUserService(IGenericService[User], ABC):

    @abstractmethod
    def GetByUsername(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def GetByNumber(self, number: str) -> Optional[User]:
        pass

    @abstractmethod
    def GetByUsernameAndPassword(self, username: str, password: str) -> Optional[User]:
        pass

    @abstractmethod
    def UpdateUserAbout(self, userID: int, name: str, surname:str) -> None:
        pass

    @abstractmethod
    def UpdateUserPassword(self, userID: int, password: str) -> None:
        pass