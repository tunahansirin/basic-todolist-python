import hashlib
from typing import Optional
from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.UserRepository import UserRepository
from EntityLayer.Concrete.User import User
from SrnToDoList.Helper.UserHelper import UserHelper
from SrnToDoList.View.ProfileUserDetailView import ProfileUserDetailView
from SrnToDoList.View.ProfileUserEditView import ProfileUserEditView
from SrnToDoList.View.ProfileView import ProfileView

# Profil ile ilgili işlemlerin yapıldığı sınıf.
class ProfileController:
    def __init__(self, pageController):
        self.pageController = pageController
        self.userHelper = UserHelper(self.pageController)

    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Profil menüsünü gösteren metot.
    def ShowProfileView(self):
        ProfileView(self.pageController).ProfileMenu()

    # Profil detaylarını gösteren metot.
    def ShowProfileUserDetailView(self):
        ProfileUserDetailView(self.pageController).ProfileUserDetail()

    # Profil düzenleme ekranını gösteren metot.
    def ShowProfileEditView(self):
        ProfileUserEditView(self.pageController).ProfileUserEditMenu()

    # -> Sınıf içerisinde kullanılnan metotlar

    # Kullanıcı detaylarını getiren metot.
    def GetUserDetail(self) -> Optional[User]:
        userManager = UserManager(UserRepository())
        username = self.userHelper.GetUserUsername()
        user = userManager.GetByUsername(username)
        return user
    
    # Kullanıcı bilgilerini güncelleyen metot.
    def ChangeUserAbout(self, name: str, surname: str) -> None:
        userManager = UserManager(UserRepository())
        user = self.GetUserDetail()
        userManager.UpdateUserAbout(user.Id, name, surname)

    # Kullanıcı şifresini güncelleyen metot.
    def ChangeUserPassword(self, password: str) -> None:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        userManager = UserManager(UserRepository())
        user = self.GetUserDetail()
        userManager.UpdateUserPassword(user.Id, hashed_password)

