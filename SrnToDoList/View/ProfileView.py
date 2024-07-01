from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Kullanıcının profil menüsünü gösteren sınıf. Kullanıcının profil detaylarını ve düzenleme işlemlerini yapmasını sağlar
class ProfileView:
    def __init__(self, controller):
        self.pageController = controller
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.loginMenuList = {
            "0": "Geri Dön",
            "1": "Profil Detayları",
            "2": "Profil Düzenle"
        }

    # Profil menüsünü gösteren metot
    def ProfileMenu(self):
        self.clearHelper.ClearConsole()

        self.writerHelper.writerMenu(menuDict = self.loginMenuList, title= 'Profil Menüsü')

        while True:
            choice = self.writerHelper.writerText(text="Lütfen bir seçenek girin: ", prompt=True)

            if choice == "0":
                self.pageController.homeController.ShowHomeView()
                break

            elif choice == "1":
                self.pageController.profileController.ShowProfileUserDetailView()
                break

            elif choice == "2":
                self.pageController.profileController.ShowProfileEditView()
                break
            
            else:
                self.writerHelper.writerText(text="Geçersiz seçim. Lütfen tekrar deneyin.", color="error")