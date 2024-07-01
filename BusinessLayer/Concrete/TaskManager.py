from typing import List
from DataAccessLayer.Abstract.ITaskDal import ITaskDal
from EntityLayer.Concrete.Task import Task
from datetime import datetime

# TaskManager sınıfı ITaskService interface'inden miras alır.
# ITaskService interface'inde tanımlı olan metodları bu sınıf içerisinde implemente ederiz
# ve bu metodları kullanarak işlemlerimizi gerçekleştiririz

class TaskManager:
    def __init__(self, taskDal: ITaskDal):
        self.taskDal = taskDal
    
    # Görev Listesinde bulunan tüm görevleri bize liste şeklinde döndüren metot.
    def GetAllTasksByListID(self, taskListID: int) -> List[Task]:
        query = "SELECT * FROM tasks WHERE ListID = %s"
        params = (taskListID,)
        return self.taskDal.GetListByFilter(query, params)

    # Görev Listesinde bulunan tamamlanmış görevleri bize liste şeklinde döndüren metot.
    def GetCompletedTasksByListID(self, taskListID: int) -> List[Task]:
        query = "SELECT * FROM tasks WHERE ListID = %s AND Status = 1"
        params = (taskListID,)
        return self.taskDal.GetListByFilter(query, params)

    # Görev Listesinde bulunan tamamlanmamış görevleri bize liste şeklinde döndüren metot.
    def GetIncompleteTasksByListID(self, taskListID: int) -> List[Task]:
        query = "SELECT * FROM tasks WHERE ListID = %s AND Status = 0"
        params = (taskListID,)
        return self.taskDal.GetListByFilter(query, params)

    # Görev silmemizi sağlayan metot.
    def DeleteTasksByTaskListID(self, taskListID: int) -> None:
        query = "DELETE FROM tasks WHERE ListID = %s"
        params = (taskListID,)
        self.taskDal.DeleteRange(query, [params])

    # Görev eklememizi sağlayan metot.
    # Burada ekleme işlemi yaparken bir listeye göre birden fazla veriyi eklememizi sağlayan metot.
    def AddRange(self, tasks: List[Task]) -> None:
        query = "INSERT INTO tasks (TaskName, Status, CompletedDate, ListID) VALUES (%s, %s, %s, %s)"
        params = [(task.TaskName, task.Status, task.CompletedDate, task.ListID) for task in tasks]
        self.taskDal.InsertRange(query, params)

    # Görevin durumunu güncellememizi sağlayan metot.
    def UpdateTaskStatus(self, taskListId: int, status: int) -> None:
        dateTime = None
        if status == 1:
            dateTime = datetime.now()

        query = "UPDATE tasks SET Status = %s, CompletedDate = %s WHERE Id = %s"
        params = (status, dateTime, taskListId)
        self.taskDal.Update(query, params)
