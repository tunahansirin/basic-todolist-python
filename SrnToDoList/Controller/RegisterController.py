from datetime import datetime
import hashlib
from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.UserRepository import UserRepository
from EntityLayer.Concrete.User import User
from SrnToDoList.Helper.GenericCode import GenericCode
from SrnToDoList.Model.UserRegisterModel import UserRegisterModel
from SrnToDoList.View.RegisterView import RegisterView

# Kayıt işlemleri ile ilgili işlemlerin yapıldığı sınıf.
class RegisterController:
    def __init__(self, pageController):
        self.pageController = pageController

    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Kayıt ekranını gösteren metot.
    def ShowRegisterView(self):
        RegisterView(self.pageController).UserRegisterInput()

    # -> Sınıf içerisinde kullanılnan metotlar
    
    # Kullanıcı kayıt işlemlerini yapan metot.
    def UserRegister(self, userRegisterModel: UserRegisterModel) -> bool:
        userManager = UserManager(UserRepository())
        genericCode = GenericCode()

        hashed_password = hashlib.sha256(userRegisterModel.Password.encode('utf-8')).hexdigest()

        user = User(Number=genericCode.GenericCodeNumberDB(), 
                    Name=userRegisterModel.Name, 
                    Surname=userRegisterModel.Surname, 
                    Username=userRegisterModel.Username, 
                    Password=hashed_password,
                    CreatedDate=datetime.now())
        
        try:
            userManager.TAdd(user)
            return True
        except ValueError as e:
            print(e)
            return False
