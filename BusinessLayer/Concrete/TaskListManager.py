from typing import List, Optional
from BusinessLayer.Abstract.ITaskListServcice import ITaskListService
from DataAccessLayer.Abstract.ITaskListDal import ITaskListDal
from EntityLayer.Concrete.TaskList import TaskList

# TaskListManager sınıfı ITaskListService interface'inden miras alır.
# ITaskListService interface'inde tanımlı olan metodları bu sınıf içerisinde implemente ederiz
# ve bu metodları kullanarak işlemlerimizi gerçekleştiririz

class TaskListManager(ITaskListService):

    def __init__(self, taskListDal: ITaskListDal):
        self.taskListDal = taskListDal

    # Görev listesi eklemimizi sağlayan metot.
    def TAdd(self, taskList: TaskList) -> None:
        query = "INSERT INTO tasklist (ListName, CreatedDate, UserID) VALUES (%s, %s, %s)"
        params = (taskList.ListName, taskList.CreatedDate, taskList.UserID)
        self.taskListDal.Insert(query, params)

    # Kullanıcı Id ve liste adına göre görev listesi getiren metot.
    def GetByUserIDAndListName(self, userID: int, listName: str) -> Optional[TaskList]:
        query = "SELECT * FROM tasklist WHERE UserID = %s AND ListName = %s"
        params = (userID, listName)
        return self.taskListDal.GetByFilter(query, params)

    # Kullanıcı Id'sine göre görev listesi getiren metot.
    def GetAllByUserID(self, userID: int) -> List[TaskList]:
        query = "SELECT * FROM tasklist WHERE UserID = %s"
        params = (userID,)
        return self.taskListDal.GetListByFilter(query, params)

    # Kullanıcı Id'sine göre görev listelerini tarihe göre sıralayan metot.
    def GetAllByUserIDOrderByDate(self, userID: int) -> List[TaskList]:
        query = "SELECT * FROM tasklist WHERE UserID = %s ORDER BY CreatedDate"
        params = (userID,)
        return self.taskListDal.GetListByFilter(query, params)

    # Kullanıcı Id'sine göre görev listesi adına göre a-z'ye sıralayan metot.
    def GetAllByUserIDOrderByNameAsc(self, userID: int) -> List[TaskList]:
        query = "SELECT * FROM tasklist WHERE UserID = %s ORDER BY ListName ASC"
        params = (userID,)
        return self.taskListDal.GetListByFilter(query, params)

    # Kullanıcı Id'sine göre görev listesi adına göre z-a'ya sıralayan metot.
    def GetAllByUserIDOrderByNameDesc(self, userID: int) -> List[TaskList]:
        query = "SELECT * FROM tasklist WHERE UserID = %s ORDER BY ListName DESC"
        params = (userID,)
        return self.taskListDal.GetListByFilter(query, params)
    
    # Görev Listesini silmemizi sağlayan metot.
    def Delete(self, taskListID: TaskList) -> None:
        query = "DELETE FROM tasklist WHERE Id = %s"
        params = (taskListID,)
        self.taskListDal.Delete(query, params)