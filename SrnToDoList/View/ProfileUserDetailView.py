from datetime import datetime
from EntityLayer.Concrete.User import User
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Kullanıcı detaylarının görüntülendiği sınıf. Kullanıcı detaylarının listelendiği metotları içerir
class ProfileUserDetailView:
    def __init__(self, pagecontroller):
        self.pagecontroller = pagecontroller
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()

    # Kullanıcı detaylarını gösteren metot
    def ProfileUserDetail(self):
        self.clearHelper.ClearConsole()
        user: User = self.pagecontroller.profileController.GetUserDetail()
        self.writerHelper.writerTitle("Kullanıcı Detayları")
        self.writerHelper.writerText(text="Hesap Numarası: " + user.Number, color="info")
        self.writerHelper.writerText(text="Ad: " + user.Name, color="info")
        self.writerHelper.writerText(text="Soyad: " + user.Surname, color="info")  # Soyad'ı düzeltildi
        self.writerHelper.writerText(text="Kullanıcı Adı: " + user.Username, color="info")
        self.writerHelper.writerText(text="Hesap Oluşturulma Tarihi: " + user.CreatedDate.strftime('%Y-%m-%d %H:%M:%S'), color="info")
        self.writerHelper.writerText(text="Geriye Dönmek İçin Enter Tuşuna Basınız", prompt=True)
        self.pagecontroller.profileController.ShowProfileView()
        return None
