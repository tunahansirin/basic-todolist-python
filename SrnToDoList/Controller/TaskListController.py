from typing import List, Optional
from BusinessLayer.Concrete.TaskListManager import TaskListManager
from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.TaskListRepository import TaskListRepository
from DataAccessLayer.Concrete.UserRepository import UserRepository
from EntityLayer.Concrete.TaskList import TaskList
from SrnToDoList.View.TaskListCreateView import TaskListCreateView
from SrnToDoList.View.TaskListDeleteView import TaskListDeleteView
from SrnToDoList.View.TaskListGetListView import TaskListGetListView
from SrnToDoList.View.TaskListView import TaskListView

# Görev Liste işlemleri ile ilgili işlemlerin yapıldığı sınıf.
class TaskListController:
    def __init__(self, pageController) -> None:
        self.pageController = pageController
        self.taskListManager = TaskListManager(TaskListRepository())

    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Görev listesi oluşturma menüsünü gösteren metot.
    def ShowCreateTaskMenuList(self) -> None:
        TaskListCreateView(self.pageController).CreateMenuList()

    # Görev listesi listeleme menüsünü gösteren metot.
    def ShowTaskListView(self) -> None:
        TaskListView(self.pageController).TaskListMenu()

    # Görev listesi son listesini gösteren metot.
    def ShowTaskLastListView(self, lastListName: str) -> None:
        TaskListGetListView(self.pageController).ShowLastList(lastListName)

    # Görev listesi oluşturma gösteren metot.
    def ShowTaskListCreateView(self) -> None:
        TaskListCreateView(self.pageController).TaskListCreateInput()

    # Görev listesi silme menüsünü gösteren metot.
    def ShowTaskListDeleteView(self) -> None:
        TaskListDeleteView(self.pageController).TaskListDeleteInput()

    # Görev listesi listeleme menüsünü gösteren metot.
    def ShowTaskListGetListView(self) -> None:
        TaskListGetListView(self.pageController).TaskListGetListMenu()

    # -> Sınıf içerisinde kullanılnan metotlar

    # Kullanıcının id değerini getiren metot.
    def _GetUserID(self) -> int:
        userManager = UserManager(UserRepository())
        username = self.pageController.sessionHelper.GetSessionById(self.pageController.sessionID)
        user = userManager.GetByUsername(username)
        return user.Id

    # Görev Listesini tarihe göre sıralayarak getiren metot.
    def GetTaskListOrderByDate(self) -> List[Optional[TaskList]]:
        return self.taskListManager.GetAllByUserIDOrderByDate(self._GetUserID())

    # Görev Listesini liste ismine göre sıralayan metot a-z.
    def GetTaskListOrderByNameAsc(self) -> List[Optional[TaskList]]:
        return self.taskListManager.GetAllByUserIDOrderByNameAsc(self._GetUserID())

    # Görev Listesini liste ismine göre sıralayan metot z-a.
    def GetTaskListOrderByNameDesc(self) -> List[Optional[TaskList]]:
        return self.taskListManager.GetAllByUserIDOrderByNameDesc(self._GetUserID())
    
    # Görev listesin tümünü getiren metot.
    def GetAllTaskLists(self) -> List[Optional[TaskList]]:
        return self.taskListManager.GetAllByUserID(self._GetUserID())

    # Görev listesini silen metot.
    def DeleteTasksByTaskListID(self, taskListID: int) -> None:
        self.taskListManager.Delete(taskListID)
