from typing import List, Optional
from BusinessLayer.Concrete.TaskManager import TaskManager
from DataAccessLayer.Concrete.TaskRepository import TaskRepository
from EntityLayer.Concrete.Task import Task
from SrnToDoList.View.TaskView import TaskView

# Görevler ile ilgili işlemlerin yapıldığı sınıf.
class TaskController:
    def __init__(self, pageController) -> None:
        self.pageController = pageController
        self.taskManager = TaskManager(TaskRepository())

    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Görev menüsünü gösteren metot.
    def ShowTaskView(self, taskListID: int, lastListName: str) -> None:
        TaskView(self.pageController).TaskMenu(taskListID, lastListName)

    # -> Sınıf içerisinde kullanılnan metotlar

    # Görev listesindeki tüm görevleri getiren metot.
    def GetAllTasks(self, taskListID: int) -> List[Optional[Task]]:
        return self.taskManager.GetAllTasksByListID(taskListID)

    # Görev listesindeki tamamlanmış görevleri getiren metot.
    def GetCompletedTasks(self, taskListID: int) -> List[Optional[Task]]:
        return self.taskManager.GetCompletedTasksByListID(taskListID)

    # Görev listesindeki tamamlanmamış görevleri getiren metot.
    def GetIncompleteTasks(self, taskListID: int) -> List[Optional[Task]]:
        return self.taskManager.GetIncompleteTasksByListID(taskListID)

    # Görev listesini silen metot.
    def DeleteTasksByTaskListID(self, taskListID: int) -> None:
        self.taskManager.DeleteTasksByTaskListID(taskListID)

    # Görev durumunu güncelleyen metot.
    def UpdateTask(self, taskListID: int, taskStatus: int) -> None:
        self.taskManager.UpdateTaskStatus(taskListID, taskStatus)
