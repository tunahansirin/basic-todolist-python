import time
from typing import Optional
from EntityLayer.Concrete.User import User
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.InputHelper import InputHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# Kullanıcı giriş işlemlerinin yapıldığı görüntü sınıfı. Burada kullanıcıdan gereken bilgiler alınır ve giriş işlemi yapılır.
class UserLoginView:
    def __init__(self, pageController):
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.inputHelper = InputHelper()
        self.sessionHelper = self.pageController.sessionHelper

    # Kullanıcı giriş ekranını gösterir ve kullanıcıdan gerekli bilgilerinin alındığı metottur.
    def UserLoginInput(self):
        self.clearHelper.ClearConsole()

        self.writerHelper.writerTitle(title="Kullanıcı Girişi")
        self.writerHelper.writerText("[Geri dönmek için 0 girin]", color="warning")

        username = self.inputHelper.getInputControl(text="Kullanıcı Adınızı Girin: ", goPage=self.pageController.loginController.ShowLoginView)
        password = self.inputHelper.getInputControl(text="Şifrenizi Girin: ", goPage=self.pageController.loginController.ShowLoginView)
        
        self.UserLogin(username, password)

    # Kullanıcı giriş işleminin yapıldığı metottur. Kullanıcı bilgileri kontrol edilir ve giriş işlemi yapılır.
    def UserLogin(self, username: str, password: str):
        result = self.pageController.loginController.UserLogin(username, password)

        if result:
            user: Optional[User] = self.pageController.loginController.GetUserInfo(username)
            session_id = self.sessionHelper.CreateSession(user.Username)
            self.pageController.sessionID = session_id
            self.writerHelper.writerText("Giriş başarılı! Yönlendiriliyorsunuz...", color="success")
            time.sleep(2)
            self.pageController.homeController.ShowHomeView()

        else:
            self.writerHelper.writerText("Giriş başarısız! Tekrar Deneyiniz..", color="error")
            time.sleep(2)
            self.pageController.loginController.ShowUserLoginView()