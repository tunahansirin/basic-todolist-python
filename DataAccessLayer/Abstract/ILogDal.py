from abc import ABC
from EntityLayer.Concrete.Log import Log
from DataAccessLayer.Abstract.IGenericDal import IGenericDal

# Generic interface'ini miras alarak Log nesnesi için CRUD işlemleri tanımlıyoruz.
class ILogDal(IGenericDal[Log], ABC):
    pass
