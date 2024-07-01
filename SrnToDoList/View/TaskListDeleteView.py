import time
from datetime import datetime
from colorama import Fore, Style
import pandas as pd
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.InputHelper import InputHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Görev listelerinin silindiği sınıf. Görev listelerinin görüntülendiği ve silindiği metotları içerir.
class TaskListDeleteView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.inputHelper = InputHelper()
        self.sessionHelper = self.pageController.sessionHelper
        self.taskListController = self.pageController.taskListController
        self.taskController = self.pageController.taskController

    def TaskListDeleteInput(self):
        self.clearHelper.ClearConsole()
        taskLists = self.taskListController.GetAllTaskLists()

        if not taskLists:
            self.writerHelper.writerTitle("Herhangi bir göreviniz bulunmamaktadır.")
            self.writerHelper.writerText(text="Geri dönmek için enter tuşuna basın!", prompt=True)
            self.pageController.taskListController.ShowTaskListView()
            return
        
        deleteMenuList = {
            "0": "Geri Dön",
            "1": "Görev Listesi Sil (Sıra numrasına göre)",
            "2": "Görev Listesi Sil (Görev liste adına göre)",
            "3": "Görev Listesi Sil (Oluşturma tarihine göre. İlk sıradaki veri silinir.)"
        }

        data = {
            'ListName': [taskList.ListName for taskList in taskLists],
            'CreatedDate': [taskList.CreatedDate for taskList in taskLists]
        }
        df = pd.DataFrame(data)
        df.index += 1

        print(Fore.LIGHTBLUE_EX + "Görev Listeleri" + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + df.to_string() + Style.RESET_ALL)

        self.writerHelper.writerMenu(deleteMenuList)
        choice = self.inputHelper.getInputControl("Silme işleminiz türü nedir (0 - Geri Dön): ", self.pageController.taskListController.ShowTaskListView)
        
        if choice in ["1", "2", "3"]:
            self.clearHelper.ClearLastLines(6)
        
        if choice == "1":
            self.DeleteTaskList(df, taskLists, "index")
        elif choice == "2":
            self.DeleteTaskList(df, taskLists, "name")
        elif choice == "3":
            self.DeleteTaskList(df, taskLists, "date")
        else:
            self.pageController.taskListController.ShowTaskListDeleteView()
    
    def DeleteTaskList(self, df, taskLists, deleteType):
        if deleteType == "index":
            index = self.getTaskIndex(df)
            if index is None:
                return
            selectedTaskList = taskLists[index - 1]

        elif deleteType == "name":
            selectedTaskList = self.getTaskListByName(df, taskLists)
            if selectedTaskList is None:
                return
            
        elif deleteType == "date":
            selectedTaskList = self.getTaskListByDate(df, taskLists)
            if selectedTaskList is None:
                return

        confirmation = self.inputHelper.getInputControl("Veriyi silmek istediğinize emin misiniz? Evet - Hayır: ", self.pageController.taskListController.ShowTaskListDeleteView)
        if confirmation.lower() == 'evet':
            self.taskController.DeleteTasksByTaskListID(selectedTaskList.Id)
            self.taskListController.DeleteTasksByTaskListID(selectedTaskList.Id)

            self.writerHelper.writerText("Görev listesi ve ilişkili görevler başarıyla silindi.", color="success")
            self.pageController.logController.AddLog(f"{selectedTaskList.ListName} adlı görev listesi ve içerisinde bulunan görevler  silindi.")
        
        time.sleep(1)
        self.pageController.taskListController.ShowTaskListDeleteView()

    def getTaskIndex(self, df):
        while True:
            try:
                index = int(self.inputHelper.getInputControl("Hangi sıra adına sahip veriyi silmek istiyorsunuz (0 - Geri Dön): ", self.pageController.taskListController.ShowTaskListDeleteView))
                if index not in df.index:
                    raise ValueError("Geçersiz sıra numarası. Lütfen tekrar deneyin.")
                return index
            except ValueError as e:
                self.clearHelper.ClearLastLine()
                self.writerHelper.writerText(str(e), color="error")

    def getTaskListByName(self, df, taskLists):
        while True:
            taskListName = self.inputHelper.getInputControl("Silmek istediğiniz görev listesinin adını girin (0 - Geri Dön): ", self.pageController.taskListController.ShowTaskListDeleteView)
            selectedTaskList = df.loc[df['ListName'] == taskListName]
            if selectedTaskList.empty:
                self.writerHelper.writerText("Belirtilen ad ile eşleşen görev listesi bulunamadı. Lütfen tekrar deneyin.", color="error")
            else:
                index = selectedTaskList.index[0]
                return taskLists[index - 1]
    
    def getTaskListByDate(self, df, taskLists):
        while True:
            createdDate = self.inputHelper.getInputControl("Silmek istediğiniz listenin oluşturma tarihini girin (YYYY-MM-DD formatında) (0 - Geri Dön): ", self.pageController.taskListController.ShowTaskListDeleteView)
            try:
                createdDate = datetime.strptime(createdDate, '%Y-%m-%d')
                selectedTaskList = df.loc[pd.to_datetime(df['CreatedDate']).dt.date == createdDate.date()]
                if selectedTaskList.empty:
                    self.writerHelper.writerText("Belirtilen tarih ile eşleşen görev listesi bulunamadı. Lütfen tekrar deneyin.", color="error")
                else:
                    index = selectedTaskList.index[0]
                    return taskLists[index - 1]
            except ValueError:
                self.writerHelper.writerText("Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatında girin.", color="error")
