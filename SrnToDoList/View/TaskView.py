import time
from colorama import Fore, Style
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper
import pandas as pd

# Görevlerin görüntülendiği sınıf. Görevlerin listelendiği ve durumlarının güncellendiği metotları içerir.
class TaskView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.taskListId = None
        self.lastListName = None
        self.menuName = None

        self.taskMenuList = {
            "0": "Geri Dön",
            "1": "Tüm Görevler",
            "2": "Tamamlanan Görevler",
            "3": "Tamamlanmamış Görevler",
        }

    # Görevlerin listelendiği menüyü gösterir. Eğer daha önceden bir görüntüleme seçimi yapıldıysa ona göre işlem yapar.
    def ShowMenu(self, taskListID, menuName):
        self.taskListId = taskListID
        self.menuName = menuName
        self.clearHelper.ClearConsole()

        if self.menuName == "All":
            self.ShowAllTasks()

        elif self.menuName == "Completed":
            self.ShowCompletedTasks()

        elif self.menuName == "InComplete":
            self.ShowIncompleteTasks()

        else:
            self.TaskMenu(taskListID)

        return None

    # Görev menüsünü gösterir. Kullanıcının seçimine göre işlem yapar.
    def TaskMenu(self, taskListID: int, lastListName: str = None):
        if lastListName is not None:
            self.lastListName = lastListName

        self.clearHelper.ClearConsole()

        self.taskListId = taskListID

        self.writerHelper.writerMenu(self.taskMenuList, 'Görev Menüsü')
        
        while True:
            choice = self.writerHelper.writerText("Lütfen bir seçenek girin: ", True)

            if choice == "0":
                self.pageController.taskListController.ShowTaskLastListView(self.lastListName)
                break
            
            elif choice == "1":
                self.ShowMenu(taskListID, "All")
                break
            
            elif choice == "2":
                self.ShowMenu(taskListID, "Completed")
                break

            elif choice == "3":
                self.ShowMenu(taskListID, "InComplete")
                break
            
            else:
                self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")

        return None

    # Tüm görevleri listeler.    
    def ShowAllTasks(self):
        tasks = self.pageController.taskController.GetAllTasks(self.taskListId)
        self.DisplayTasks(tasks)

    # Tamamlanan görevleri listeler.
    def ShowCompletedTasks(self):
        tasks = self.pageController.taskController.GetCompletedTasks(self.taskListId)
        self.DisplayTasks(tasks)

    # Tamamlanmamış görevleri listeler.
    def ShowIncompleteTasks(self):
        tasks = self.pageController.taskController.GetIncompleteTasks(self.taskListId)
        self.DisplayTasks(tasks)

    # Görevleri Listeler
    def DisplayTasks(self, tasks):
        self.clearHelper.ClearConsole()

        if not tasks:
            self.writerHelper.writerText("Görev bulunamadı. Geri dönmek için bir tuşa basın.", color="info")
            input("Devam etmek için bir tuşa basın...")
            self.TaskMenu(self.taskListId, self.lastListName)
            return

        taskData = [
            {
                "Görev Adı": task.TaskName,
                "Görev Durumu": "Tamamlandı" if task.Status == 1 else "Tamamlanmadı"
            }
            for task in tasks
        ]
        df = pd.DataFrame(taskData, index=range(1, len(taskData) + 1))

        print(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + df.to_string() + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)

        self.updateTaskStatus(tasks)
        return None

    # Görev durumunu günceller.
    def updateTaskStatus(self, tasks):
        while True:
            user_input = self.writerHelper.writerText("Durumunu güncellemek istediğiniz görevin yanında bulunan numarasını girin (Geri dönmek için '0' girin): ", True)
            if user_input == "0":
                self.TaskMenu(self.taskListId, self.lastListName)
                break

            try:
                task_number = int(user_input)
                if task_number < 1 or task_number > len(tasks):
                    self.writerHelper.writerText("Geçersiz görev numarası.", color="error")
                    continue
                
                else:
                    # Görev numarasını sıfırdan başlayan ID'ye dönüştürmek için:
                    task_id = tasks[task_number - 1].Id
                    
                    new_status = 1 if tasks[task_number - 1].Status == 0 else 0
                    self.pageController.taskController.UpdateTask(task_id, new_status)
                    self.writerHelper.writerText("Görev durumu güncellendi.", color="success")

                    self.pageController.logController.AddLog(f"{tasks[task_number - 1].TaskName} görevinin durumu güncellendi. yeni durum: {'Tamamlandı' if new_status == 1 else 'Tamamlanmadı'}.")
                    time.sleep(1)
                    self.ShowMenu(self.taskListId, self.menuName)
                    break

            except ValueError:
                self.writerHelper.writerText("Lütfen geçerli bir numara girin.", color="error")
        
        return None
