import hashlib
from typing import Optional
from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.UserRepository import UserRepository
from EntityLayer.Concrete.User import User
from SrnToDoList.View.LoginView import LoginView
from SrnToDoList.View.UserLoginView import UserLoginView

# Kullanıcı giriş işlemlerinin yapıldığı sınıf.
class LoginController:
    def __init__(self, pageController) -> None:
        self.pageController = pageController
        self.userManager = UserManager(UserRepository())

    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Giriş ekranını gösteren metot.
    def ShowLoginView(self) -> None:
        LoginView(self.pageController).LoginMenu()

    # Kullanıcı giriş ekranını gösteren metot.
    def ShowUserLoginView(self) -> None:
        UserLoginView(self.pageController).UserLoginInput()

    # -> Sınıf içerisinde kullanılnan metotlar

    # Kullanıcı bilgilerini getirir.
    def GetUserInfo(self, username)  -> Optional[User]:
        try:
            user = self.userManager.GetByUsername(username)
            if user is None:
                return None
            return user
        except ValueError as e:
            print(e)
            return None

    # Kullanıcı giriş işlemlerini yapar.
    def UserLogin(self, username, password)  -> bool:
        # Burada türkçe karakterler için utf-8 encoding yapılıyor.
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        try:
            user = self.userManager.GetByUsernameAndPassword(username, hashed_password)
            if user is None:
                return False
            return True
        except ValueError as e:
            print(e)
            return False