from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

# Diğer servislerin implemente edeceği interface
# Burada genel olarak kullanacak metotlar tanımlanmıştır

class IGenericService(ABC, Generic[T]):
    
    @abstractmethod
    def TAdd(self, entity: T) -> None:
        pass
