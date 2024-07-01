import time
from BusinessLayer.Validator.UsersValidator import UserValidator
from SrnToDoList.Helper.GenericCode import GenericCode
from SrnToDoList.Helper.InputHelper import InputHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper
from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Model.UserRegisterModel import UserRegisterModel

# Kullanıcı kayıt işlemlerinin yapıldığı görüntü sınıfı. Burada kullanıcıdan gereken bilgiler alınır ve kayıt işlemi yapılır
class RegisterView:
    def __init__(self, pageController) -> None:
        self.pageController = pageController
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()
        self.userValidator = UserValidator()
        self.inputHelper = InputHelper()

    # Kullanıcı kayıt ekranını gösterir ve kullanıcıdan gerekli bilgilerinin alındığı metottur
    def UserRegisterInput(self):
        self.clearHelper.ClearConsole()
        self.writerHelper.writerTitle(title="Kullanıcı Kayıt Ol")
        self.writerHelper.writerText("[Geri dönmek için 0 girin]", color="warning")

        name = self.inputHelper.getInputControl(text="Adınızı girin: ", goPage=self.pageController.mainController.ShowMainView, validationFunction=self.userValidator.ValidateName)
        surname = self.inputHelper.getInputControl(text="Soyadınızı girin: ", goPage=self.pageController.mainController.ShowMainView, validationFunction=self.userValidator.ValidateSurname)
        username = self.inputHelper.getInputControl(text="Kullanıcı adınızı girin: ", goPage=self.pageController.mainController.ShowMainView, validationFunction=self.userValidator.ValidateUsername)
        password = self.inputHelper.getInputControl(text="Şifrenizi girin: ", goPage=self.pageController.mainController.ShowMainView, validationFunction=self.userValidator.ValidatePassword)

        self.UserRegister(UserRegisterModel(Name=name, Surname=surname, Username=username, Password=password))


    # Kullanıcı kayıt işleminin yapıldığı metottur. Kullanıcı bilgileri kontrol edilir ve kayıt işlemi yapılır
    def UserRegister(self, userRegisterModel: UserRegisterModel):
        result = self.pageController.registerController.UserRegister(userRegisterModel)

        if result:
            self.writerHelper.writerText("Kayıt başarılı! Yönlendiriliyorsunuz...", color="success")
            time.sleep(2)
            self.pageController.loginController.ShowUserLoginView()
            
        else:
            self.writerHelper.writerText("Kayıt başarısız!", color="error")
            self.pageController.homeController.ShowHomeView()
        
        return None
