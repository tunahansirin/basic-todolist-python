from DataAccessLayer.Abstract.ITaskListDal import ITaskListDal
from DataAccessLayer.Concrete.GenericRepository import GenericRepository
from EntityLayer.Concrete.TaskList import TaskList

# TaskList verilerinin veritabanı işlemlerinin yapıldığı sınıf
class TaskListRepository(GenericRepository[TaskList], ITaskListDal):

    # Burada GenericRepository sınıfından miras alınarak TaskList verilerinin veritabanı işlemleri yapılmıştır.
    def __init__(self):
        super().__init__(TaskList)