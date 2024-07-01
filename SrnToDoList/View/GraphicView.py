from colorama import Fore, Style
import pandas as pd
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper
from SrnToDoList.Helper.GraphicsHelper import GraphicsHelper

# Grafik ile ilgili görünüm işlemlerini gerçekleştirildiği sınıftır
class GraphicView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()

        self.graphicMenuList = {
            "0": "Geri Dön",
            "1": "Pasta Grafiği",
            "2": "Histogram Grafiği",
            "3": "Saçılma Grafiği",
        }
    

    # Burada Görev listeleri listeleniyor ve kullanıcıdan seçim yapılamsı bekleniyor
    def GraphicMenu(self):
        self.clearHelper.ClearConsole()

        taskList = self.pageController.taskListController.GetAllTaskLists()
        if len(taskList) <= 0:
            self.writerHelper.writerText("Görev listesi bulunamadı. Lütfen önce görev listesi oluşturun.", color="warning")
            self.writerHelper.writerText("Geriye dönmek için enter tuşuna basın!", prompt=True)
            self.pageController.taskListController.ShowTaskListView()
            return
        
        data = {
            'Görev Listesi Adı ': [],
            'Oluşturma Tarihi ': []
        }
        
        for t in taskList:
            if t:
                data['Görev Listesi Adı '].append(t.ListName)
                data['Oluşturma Tarihi '].append(t.CreatedDate)

        df = pd.DataFrame(data)
        df.index += 1

        print(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + df.to_string() + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)

        self.writerHelper.writerText("[Geri dönmek için 0 girin]", color="warning")

        if len(taskList) == 1:
            prompt_text = "Bir görev listesi seçin: "
        else:
            prompt_text = "Bir görev listesi seçin (1 ile {} arasında): ".format(len(taskList))

        while True:
            try:
                index = int(self.writerHelper.writerText(text=prompt_text, prompt=True))

                if 1 <= index <= len(taskList):
                    selectedTask = taskList[index - 1]
                    break

                elif index == 0:
                    self.pageController.taskListController.ShowTaskListView()
                    return

                else:
                    self.writerHelper.writerText(text="Geçersiz seçim. Lütfen tabloda bulunan aralıkta bir sayı girin.", color="error")

            except ValueError:
                self.writerHelper.writerText(text="Geçersiz giriş. Lütfen bir sayı girin.", color="error")

        # Seçilen görev listesi için grafik menüsünü göster
        self.ShowGraphicMenu(selectedTask)
    
    # Grafik menüsünü gösteren metot
    def ShowGraphicMenu(self, selectedTask):
        self.clearHelper.ClearConsole()

        print(Fore.LIGHTBLUE_EX + "Seçilen Görev Listesi: " + selectedTask.ListName + Style.RESET_ALL)
        self.writerHelper.writerMenu(self.graphicMenuList)

        while True:
            choice = self.writerHelper.writerText(text="Bir grafik türü seçin (0 - Geri Dön): ", prompt=True)
            if choice == "0":
                self.pageController.taskListController.ShowTaskListView()
                return
            elif choice in ["1", "2", "3"]:
                self.GenerateGraph(choice, selectedTask)
                break
            else:
                self.writerHelper.writerText(text="Geçersiz seçim. Lütfen 0-3 arasında bir değer girin.", color="error")
    
    # Seçilen grafik türüne göre grafik oluşturulan metot
    def GenerateGraph(self, choice, selectedTask):
        data = {
            'Status': [task.Status for task in self.pageController.taskController.GetAllTasks(selectedTask.Id)]
        }
        df = pd.DataFrame(data)

        graphicHelper = GraphicsHelper(df)

        if choice == "1":
            graphicHelper.PieGraphic()
        elif choice == "2":
            graphicHelper.HistogramGraphic()
        elif choice == "3":
            graphicHelper.ScatterGraphic()

        self.ShowGraphicMenu(selectedTask)