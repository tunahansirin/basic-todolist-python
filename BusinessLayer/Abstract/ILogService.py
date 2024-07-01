from abc import ABC
from typing import List
from BusinessLayer.Abstract.IGenericService import IGenericService
from EntityLayer.Concrete.Log import Log

# ILogService interface'i IGenericService interface'inden miras alır.

class ILogService(IGenericService[Log], ABC):
    pass