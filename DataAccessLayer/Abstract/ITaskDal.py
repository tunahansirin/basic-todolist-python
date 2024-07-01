from abc import ABC
from EntityLayer.Concrete.Task import Task
from DataAccessLayer.Abstract.IGenericDal import IGenericDal

# Generic interface'ini miras alarak Log nesnesi için CRUD işlemleri tanımlıyoruz.
class ITaskDal(IGenericDal[Task], ABC):
    pass
