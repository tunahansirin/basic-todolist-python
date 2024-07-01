from BusinessLayer.Concrete.TaskListManager import TaskListManager
from BusinessLayer.Concrete.TaskManager import TaskManager
from BusinessLayer.Concrete.UserManager import UserManager
from BusinessLayer.Validator.TaskListValidator import TaskListValidator
from BusinessLayer.Validator.TaskValidator import TaskValidator
from DataAccessLayer.Concrete.TaskListRepository import TaskListRepository
from DataAccessLayer.Concrete.TaskRepository import TaskRepository
from EntityLayer.Concrete.Task import Task
from EntityLayer.Concrete.TaskList import TaskList
from EntityLayer.Concrete.User import User
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.FileHelper import FileHelper
from SrnToDoList.Helper.InputHelper import InputHelper
from SrnToDoList.Helper.UserHelper import UserHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper
from datetime import datetime
import time

# Görev listesinin oluşturulduğu sınıf. Burada görev listesi görüntülenir ve kullanıcıyla etkileşime geçilir
class TaskListCreateView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.inputHelper = InputHelper()
        self.userHelper = UserHelper(self.pageController)
        self.sessionHelper = self.pageController.sessionHelper
        self.createMenuList = {
            "0": "Geri Dön",
            "1": "Görev Listesi Oluştur",
            "2": "Excel Dosyasıyla Görev Listesi Oluştur"
        }

    # Görev listesi oluşturulduğu menüyü görüntüleyen ve kullanıcının seçim yapmasını sağlayan metot
    def CreateMenuList(self):
        self.clearHelper.ClearConsole()
        self.writerHelper.writerMenu(self.createMenuList, "Görev Listesi Oluştur Menüsü")

        while True:
            choice = self.writerHelper.writerText("Lütfen bir seçenek girin: ", True)

            if choice == "0":
                self.pageController.taskListController.ShowTaskListView()
            
            elif choice == "1":
                self.TaskListCreateInput()

            elif choice == "2":
                self.TaskListCreateExcel()

            else:
                self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")

    # Görev listesi oluşturulurken görev sayısının en az 3 olup olmadığını kontrol eden metot
    def _ValidationListCount(self, listCount):
        try:
            tListCount = int(listCount)
            if tListCount < 3:
                raise ValueError("En az 3 görev girilmesi gerekmektedir.")
            return tListCount
        except ValueError:
            raise ValueError("Geçerli bir sayı girilmelidir ve en az 3 olmalıdır.")
    
    # Görev listesi isminin veritabanına kaydedildiği metot
    def _saveTaskList(self, listName: str) -> int:
        taskListManager = TaskListManager(TaskListRepository())
        taskList = TaskList(
            CreatedDate=datetime.now(),
            ListName=listName,
            UserID=self.userHelper.GetUserId()
        )
        taskListManager.TAdd(taskList)
        return taskListManager.GetByUserIDAndListName(taskList.UserID, taskList.ListName).Id
    
    # Görevlerin veritabanına kaydedildiği metot
    def _saveTask(self, taskList: list[Task], ListId: int):
        taskManager = TaskManager(TaskRepository())

        _taskList = []

        for task in taskList:
            _taskList.append(Task(
                TaskName=task,
                CompletedDate=None,
                Status=0,
                ListID=ListId
            ))
        
        taskManager.AddRange(_taskList)

    # Görev listesi ve görevlerin veritabanına kaydedildiği metot
    def _save(self, listName: str, taskList: list[str]):
        listID = self._saveTaskList(listName)
        self._saveTask(taskList, listID)
        
    # Görev listesi oluşturulduğu metot
    def TaskListCreateInput(self):
        self.clearHelper.ClearConsole()
        userID = self.userHelper.GetUserId()
        self.writerHelper.writerTitle("Görev Listesi Oluştur")
        self.writerHelper.writerText("[Geri dönmek için 0 girin]", color="warning")
        taskListValidator = TaskListValidator(userID)
        taskValidator = TaskValidator()

        listName = self.inputHelper.getInputControl(
            text="Görev Listesi adını giriniz: ",
            goPage=self.CreateMenuList,
            validationFunction=taskListValidator.ValidateListName
        )

        listCount = self.inputHelper.getInputControl(
            text="Kaç tane görev gireceksiniz (En az 3 görev olması gerekmektedir.): ",
            goPage=self.CreateMenuList,
            validationFunction=self._ValidationListCount
        )
        
        taskList = []

        for i in range(int(listCount)):
            while True:
                taskName = self.inputHelper.getInputControl(
                    text=f"{i+1}. Görevi giriniz: ",
                    goPage=self.CreateMenuList,
                    validationFunction=taskValidator.ValidateTaskName
                )
                if taskName in taskList:
                    self.writerHelper.writerText("Bu görev adı zaten girilmiş. Lütfen farklı bir görev adı girin.", color="error")
                else:
                    taskList.append(taskName)
                    break

        self._save(listName, taskList)
        self.writerHelper.writerText("Görev listesi başarıyla oluşturuldu.", color="success")
        time.sleep(2)
        self.pageController.logController.AddLog(f"{listName} adlı görev listesi oluşturuldu.")
        
        self.pageController.taskListController.ShowTaskListGetListView()

    # Excel dosyası ile görev listesi oluşturulduğu metot
    def TaskListCreateExcel(self):
        while True:
            self.clearHelper.ClearConsole()

            self.writerHelper.writerTitle("Görev Listesi Oluştur - Excel Dosyasıyla")
            self.writerHelper.writerText("[Geri dönmek için 0 girin]", color="warning")

            fileUrl = self.inputHelper.getInputControl(
                text="Excel dosyasının yolunu giriniz: ",
                goPage=self.CreateMenuList,
            )

            fileUrl.replace("\\", "/")

            fileHelper = FileHelper(fileUrl)
            taskContent = fileHelper.ProcessFile(userID=self.userHelper.GetUserId())
            if taskContent is not None:
                for key, value in taskContent.items():
                    self._save(key, value)

                self.writerHelper.writerText("Görev listesi başarıyla oluşturuldu.", color="success")
                time.sleep(3)
                self.pageController.taskListController.ShowTaskListView()
                break