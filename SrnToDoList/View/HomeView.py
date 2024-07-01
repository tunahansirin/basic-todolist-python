import time
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Kullanıcının ana menüsünü gösteren sınıf. Kullanıcının ana menüde yapabileceği işlemleri gösterir
class HomeView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.sessionHelper = self.pageController.sessionHelper

        self.homeMenuList = {
            "0": "Oturum Kapat",
            "1": "Görev Listesi İşlemleri",
            "2": "Profil İşlemleri",
        }

    # Ana menüyü gösteren metot
    def HomeMenu(self):
        self.clearHelper.ClearConsole()

        sessionID = self.pageController.sessionID
        username = self.sessionHelper.GetSessionById(sessionID)
        if username:
            self.writerHelper.writerText(f"Hoş geldin, {username}!", color="success")
            time.sleep(1)
            self.clearHelper.ClearLastLines(1)
        else:
            self.writerHelper.writerText("Geçersiz oturum kimliği. Lütfen tekrar giriş yapın.", color="error")
            self.pageController.loginController.ShowLoginView()
            return

        self.writerHelper.writerMenu(self.homeMenuList, 'Ana Menü')
        
        while True:
            choice = self.writerHelper.writerText("Lütfen bir seçenek girin: ", True)

            if choice == "0":
                self.sessionHelper.DeleteSession(sessionID)
                
                time.sleep(1)
                self.pageController.loginController.ShowLoginView()
                break
            
            elif choice == "1":
                self.pageController.taskListController.ShowTaskListView()
                break
            
            elif choice == "2":
                self.pageController.profileController.ShowProfileView()
                break

            else:
                self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")
