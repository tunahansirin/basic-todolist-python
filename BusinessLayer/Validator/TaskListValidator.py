from BusinessLayer.Concrete.TaskListManager import TaskListManager
from DataAccessLayer.Concrete.TaskListRepository import TaskListRepository
from DataAccessLayer.Concrete.TaskRepository import TaskRepository

# TaskListValidator sınıfı, görev listesiyle ilgili bilgilerin doğruluğunu kontrol eder.
class TaskListValidator:

    def __init__(self, userID: int) -> None:
        self.taskListManager = TaskListManager(TaskListRepository())
        self.userID = userID
    
    def ValidateListName(self, listName: str):
        if not listName:
            raise ValueError("Liste adı boş olamaz")
        
        if len(listName) < 3:
            raise ValueError("Liste adı en az 3 karakter uzunluğunda olmalıdır")
        
        if self.taskListManager.GetByUserIDAndListName(self.userID , listName) is not None:
            raise ValueError(f" '{listName}' isimde bir liste bulunmaktadır. Lütfen farklı bir liste ismi giriniz.")