
from datetime import datetime
from BusinessLayer.Concrete.LogManager import LogManager
from DataAccessLayer.Concrete.LogRepository import LogRepository
from EntityLayer.Concrete.Log import Log
from SrnToDoList.Helper.UserHelper import UserHelper

# Log işlemlerinin yapıldığı sınıf
class LogController:
    def __init__(self, pageController) -> None:
        self.pageController = pageController
        self.logManager = LogManager(LogRepository())
        self.userHelper = UserHelper(self.pageController)

    # -> Sınıf içerisinde kullanılnan metotlar

    # Log ekleme işlemi
    def AddLog(self, message: str) -> None:
       
        log = Log(
            LogMessage=message,
            LogDate=datetime.now(),
            UserID=self.userHelper.GetUserId()
        )
        self.logManager.TAdd(log)

  