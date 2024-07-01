from DataAccessLayer.Abstract.ITaskDal import ITaskDal
from DataAccessLayer.Concrete.GenericRepository import GenericRepository
from EntityLayer.Concrete.Task import Task

# Task verilerinin veritabanı işlemlerinin yapıldığı sınıf
class TaskRepository(GenericRepository[Task], ITaskDal):

    # Burada GenericRepository sınıfından miras alınarak Task verilerinin veritabanı işlemleri yapılmıştır.
    def __init__(self):
        super().__init__(Task)
