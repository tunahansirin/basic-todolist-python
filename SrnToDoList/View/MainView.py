import time
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper
import os

# Ana menüyü gösteren sınıf. Kullanıcının giriş yapma, kayıt olma ve çıkış yapma işlemlerini yapmasını sağlayan metot
class MainView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()

        self.mainMenuList = {
            "0": "Çıkış Yap",
            "1": "Giriş Yap",
            "2": "Kayıt Ol",
        }

    # Ana menüyü gösteren metot
    def MainMenu(self):
        self.clearHelper.ClearConsole()

        self.writerHelper.writerMenu(self.mainMenuList, 'Srn To-Do List')
        
        while True:
            choice = self.writerHelper.writerText("Lütfen bir seçenek girin: ", True)

            if choice == "0" or choice == "exit":
                self.clearHelper.ClearConsole()
                self.writerHelper.writerText("Çıkış Yapılıyor...", color="warning")
                time.sleep(1)
                self.clearHelper.ClearConsole()
                os._exit(0)
            
            elif choice == "1":
                self.pageController.loginController.ShowLoginView()
                break

            elif choice == "2":
                self.pageController.registerController.ShowRegisterView()
                break

            else:
                self.writerHelper.writerText("Geçersiz seçim. Lütfen tekrar deneyin.", color="error")
