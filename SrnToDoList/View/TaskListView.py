from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Görev listesi menüsünün görüntülendiği ana sınıf. Görev listelerinin listelendiği ve işlemlerinin yapıldığı metotları içerir.
class TaskListView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()

        self.taskListMenuList = {
            "0": "Geri Dön",
            "1": "Görev Listesi Listele",
            "2": "Görev Listesi Oluştur",
            "3": "Görev Listesi Sil",
            "4": "Görev Listesi Grafik Görüntüle",
        }

    # Görev listesi menüsünü gösterir.
    def TaskListMenu(self):
        self.clearHelper.ClearConsole()

        self.writerHelper.writerMenu(self.taskListMenuList, 'Görev Listesi Menüsü')
        
        while True:
            choice = self.writerHelper.writerText("Lütfen bir seçenek girin: ", True)

            if choice == "0":
                self.pageController.homeController.ShowHomeView()
                break
            
            elif choice == "1":
                self.pageController.taskListController.ShowTaskListGetListView()
                break

            elif choice == "2":
                self.pageController.taskListController.ShowCreateTaskMenuList()
                break

            elif choice == "3":
                self.pageController.taskListController.ShowTaskListDeleteView()
                break

            elif choice == "4":
                self.pageController.graphicController.ShowGraphicMenu()
                break
            
            else:
                self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")

        return None
