from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Giriş menüsünün görüntülendiği ana sınıf. Kullanıcı giriş işlemlerinin yapıldığı metotları içerir
class LoginView:
    def __init__(self, controller):
        self.controller = controller
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.loginMenuList = {
            "0": "Geri Dön",
            "1": "Kullanıcı Giriş",
        }

    # Giriş menüsünü gösteren metot
    def LoginMenu(self):
        self.clearHelper.ClearConsole()

        self.writerHelper.writerMenu(menuDict = self.loginMenuList, title= 'Giriş Menüsü')

        while True:
            choice = self.writerHelper.writerText(text="Lütfen bir seçenek girin: ", prompt=True)

            if choice == "0":
                self.controller.mainController.ShowMainView()
                break

            elif choice == "1":
                self.controller.loginController.ShowUserLoginView()
                break

            else:
                self.writerHelper.writerText(text="Geçersiz seçim. Lütfen tekrar deneyin.", color="error")