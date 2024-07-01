
from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.UserRepository import UserRepository

# UserHelper sınıfı, kullanıcı işlemleri için yardımcı sınıftır.
class UserHelper:

    def __init__(self, pageController) -> None:
        self.pageController = pageController
        self.sessionHelper = self.pageController.sessionHelper;
        self.userManager = UserManager(UserRepository())

    # GetUserId metodu, oturum açmış kullanıcının Id'sini döndürür.
    def GetUserId(self):
        username = self.sessionHelper.GetSessionById(self.pageController.sessionID)
        user = self.userManager.GetByUsername(username)
        return user.Id
    
    def GetUserUsername(self):
        return self.sessionHelper.GetSessionById(self.pageController.sessionID)