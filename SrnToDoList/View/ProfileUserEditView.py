import hashlib
import time
from BusinessLayer.Validator.UsersValidator import UserValidator
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.InputHelper import InputHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Kullanıcının profil bilgilerini düzenlediği sınıf. Kullanıcının ad, soyad ve şifre bilgilerini güncelleyebilir
class ProfileUserEditView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.inputHelper = InputHelper()
        self.userEditProfile = {
            "0": "Geri Dön",
            "1": "Kişisel Bilgileri Düzenle",
            "2": "Şifre Değiştir",
        }

    # Kullanıcının profil düzenleme menüsünü gösteren metot
    def ProfileUserEditMenu(self):
        self.clearHelper.ClearConsole()

        self.writerHelper.writerMenu(menuDict=self.userEditProfile, title='Profil Düzenleme Menüsü')

        while True:
            choice = self.writerHelper.writerText(text="Lütfen bir seçenek girin: ", prompt=True)

            if choice == "0":
                self.pageController.profileController.ShowProfileView()
                break

            elif choice == "1":
                self.EditPersonalInfo()
                break

            elif choice == "2":
                self.ChangePassword()
                break
            
            else:
                self.writerHelper.writerText(text="Geçersiz seçim. Lütfen tekrar deneyin.", color="error")

    # Kullanıcının ad ve soyad bilgilerini güncellemesini sağlayan metot
    def EditPersonalInfo(self):
        self.userValidator = UserValidator()
        self.clearHelper.ClearConsole()
        self.writerHelper.writerTitle("Kişisel Bilgileri Düzenle")
        self.writerHelper.writerText("Geri dönmek için '0' tuşuna basınız.", color="warning")


        name = self.inputHelper.getInputControl(text="Yeni Ad: ", goPage=self.ProfileUserEditMenu, validationFunction=self.userValidator.ValidateName)
        surname = self.inputHelper.getInputControl(text="Yeni Soyad: ", goPage=self.ProfileUserEditMenu, validationFunction=self.userValidator.ValidateSurname)

        self.pageController.profileController.ChangeUserAbout(name, surname)
        self.writerHelper.writerText(text="Kişisel bilgiler başarıyla güncellendi.", color="success")
        time.sleep(2)
        self.ProfileUserEditMenu()

    # Kullanıcının şifresini değiştirmesini sağlayan metot
    def PasswordControl(self, newPassword, confirmPassword):
        if newPassword != confirmPassword:
            raise ValueError("Şifreler eşleşmiyor. Lütfen tekrar deneyin.")
    
    # Kullanıcının mevcut şifresini kontrol eden metot
    def currentPasswordControl(self, currentPassword):
        hashed_currentPassword = hashlib.sha256(currentPassword.encode('utf-8')).hexdigest()
        if hashed_currentPassword != self.pageController.profileController.GetUserDetail().Password:
            raise ValueError("Mevcut şifrenizi yanlış girdiniz. Lütfen tekrar deneyin.")

    # Kullanıcının şifresini değiştirmesini sağlayan metot
    def ChangePassword(self):
        self.clearHelper.ClearConsole()
        self.userValidator = UserValidator()
        self.writerHelper.writerTitle("Şifre Değiştir")
        self.writerHelper.writerText("Geri dönmek için '0' tuşuna basınız.", color="warning")

        try:
            self.inputHelper.getInputControl(text="Mevcut Şifre: ", goPage=self.ProfileUserEditMenu, validationFunction=self.currentPasswordControl)
            newPassword = None

            while True:
                try:
                    newPassword = self.inputHelper.getInputControl(text="Yeni Şifre: ", goPage=self.ProfileUserEditMenu, validationFunction=self.userValidator.ValidatePassword)
                    if newPassword == "0":
                        self.ProfileUserEditMenu()
                        break

                    confirmPassword = self.inputHelper.getInputControl(text="Yeni Şifre (Tekrar): ", goPage=self.ProfileUserEditMenu)
                    if confirmPassword == "0":
                        self.ProfileUserEditMenu()
                        break

                    self.PasswordControl(newPassword, confirmPassword)
                    break

                except ValueError as error:
                    self.writerHelper.writerText(text=str(error), color="error")

            self.pageController.profileController.ChangeUserPassword(newPassword)
            self.writerHelper.writerText(text="Şifre başarıyla değiştirildi.", color="success")
            time.sleep(2)

        except ValueError as error:
            self.writerHelper.writerText(text=str(error), color="error")

        self.ProfileUserEditMenu()
