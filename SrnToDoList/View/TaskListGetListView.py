import time
from colorama import Fore, Style
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper
import pandas as pd

# Görev listelerinin görüntülendiği sınıf. Görev listelerinin listelendiği ve işlemlerinin yapıldığı metotları içerir
class TaskListGetListView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.lastList = None

    # Son görüntülenen görev listesini gösteren metot
    def ShowLastList(self, lastListName):
        if lastListName == "nameAsc":
            return self.ShowTaskListByNameAsc()

        elif lastListName == "nameDesc":
            return self.ShowTaskListByNameDesc()

        elif lastListName == "byDate":
            return self.ShowTaskListByDate()

    # Son görüntülenen görev listesinin adını gösteren metot 
    # Burası log için kullanılır.
    def ShowLastListString(self, lastListName):
        if lastListName == "nameAsc":
            return "Tarih sırasına göre görev listeleri görüntülendi."

        elif lastListName == "nameDesc":
            return "Ters alfabetik sıraya göre görev listeleri görüntülendi."

        elif lastListName == "byDate":
            return "Alfabetik sıraya göre görev listeleri görüntülendi."

    # Görev listelerini tarihe göre sıralayarak listeyen metot
    def ShowTaskListByDate(self):
        taskList = self.pageController.taskListController.GetTaskListOrderByDate()
        self.DisplayTaskList(taskList)
        return None 

    # Görev listelerini isme göre A-Z sıralayarak listeleyen metot
    def ShowTaskListByNameAsc(self):
        taskList = self.pageController.taskListController.GetTaskListOrderByNameAsc()
        self.DisplayTaskList(taskList)
        return None 

    # Görev listelerini isme göre Z-A sıralayarak listeleyen metot
    def ShowTaskListByNameDesc(self):
        taskList = self.pageController.taskListController.GetTaskListOrderByNameDesc()
        self.DisplayTaskList(taskList)
        return None 

    # Görev listelerini ekrana yazdırır ve seçim yapılmasını sağlayan metot
    def DisplayTaskList(self, taskList):
        self.pageController.logController.AddLog(f"Görev listeleri görüntülendi. {self.ShowLastListString(self.lastList)}")

        self.clearHelper.ClearConsole()
        if taskList:
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
                        selectedTask = taskList[index - 1]  # Kullanıcı 1'den başlattığı için 1 çıkartıyoruz
                        self.pageController.taskController.ShowTaskView(selectedTask.Id, self.lastList)
                        break

                    elif index == 0:
                        self.pageController.taskListController.ShowTaskListGetListView()
                        break

                    else:
                        self.writerHelper.writerText(text="Geçersiz seçim. Lütfen tabloda bulunan aralıkta bir sayı girin.", color="error")

                except ValueError:
                    self.writerHelper.writerText(text="Geçersiz giriş. Lütfen bir sayı girin.", color="error")
                    
        else:
            self.writerHelper.writerText(text="Görev listesi bulunamadı. Bir önceki sayfaya yönlendiriliyorsunuz...", color="warning")
            time.sleep(2)
            self.pageController.taskListController.ShowTaskListView()

        return None

    # Görev listesi menüsünü gösteren metot
    def TaskListGetListMenu(self):
        self.clearHelper.ClearConsole()

        taskList = self.pageController.taskListController.GetTaskListOrderByDate()
        if not taskList:
            menu_list = {
                "0": "Geri Dön"
            }
            self.writerHelper.writerMenu(menu_list, "Görev Listesi Menüsü")
            self.writerHelper.writerText(text="Görev listesi bulunmamaktadır.", color="warning")
            while True:
                choice = self.writerHelper.writerText(text="Bir seçim yapın: ", prompt=True)
                if choice == "0":
                    self.pageController.taskListController.ShowTaskListView()
                    break

                else:
                    self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")
        else:
            menu_list = {
                "0": "Geri Dön",
                "1": "Görev Listesi (Tarihe Göre Listele)",
                "2": "Görev Listesi (Alfabetik sıraya göre A-Z)",
                "3": "Görev Listesi (Alfabetik sıraya göre Z-A)"
            }
            self.writerHelper.writerMenu(menu_list, "Görev Listesi Menüsü")

            while True:
                choice = self.writerHelper.writerText(text="Bir seçim yapın: ", prompt=True)

                if choice == "0":
                    self.pageController.taskListController.ShowTaskListView()
                    break
                
                elif choice == "1":
                    self.lastList = "byDate"
                    self.ShowTaskListByDate()
                    break
                
                elif choice == "2":
                    self.lastList = "nameAsc"
                    self.ShowTaskListByNameAsc()
                    break

                elif choice == "3":
                    self.lastList = "nameDesc"
                    self.ShowTaskListByNameDesc()
                    break

                else:
                    self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")

        return  None