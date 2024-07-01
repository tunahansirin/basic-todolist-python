from abc import ABC
from DataAccessLayer.Abstract.IGenericDal import IGenericDal
from EntityLayer.Concrete.TaskList import TaskList

# Generic interface'ini miras alarak Log nesnesi için CRUD işlemleri tanımlıyoruz.
class ITaskListDal(IGenericDal[TaskList], ABC):
    pass
