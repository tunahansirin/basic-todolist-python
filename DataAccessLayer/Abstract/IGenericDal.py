from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic, List

T = TypeVar('T')

# Burada Generic bir interface oluşturuyoruz. Bu interface içerisinde CRUD işlemleri için gerekli olan metotları tanımlıyoruz.
class IGenericDal(ABC, Generic[T]):

    @abstractmethod
    def Insert(self, query: str, params: tuple) -> None:
        pass

    @abstractmethod
    def GetByFilter(self, query: str, params: tuple) -> Optional[T]:
        pass

    @abstractmethod
    def GetListByFilter(self, query: str, params: tuple) -> List[Optional[T]]:
        pass

    @abstractmethod
    def InsertRange(self, query: str, params_list: List[tuple]) -> None:
        pass

    @abstractmethod
    def Delete(self, query: str, params: tuple) -> None:
        pass

    @abstractmethod
    def DeleteRange(self, query: str, params_list: List[tuple]) -> None:
        pass

    @abstractmethod
    def Update(self, query:str , params: tuple) ->None:
        pass
