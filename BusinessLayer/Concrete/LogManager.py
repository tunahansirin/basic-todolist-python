from BusinessLayer.Abstract.ILogService import ILogService
from DataAccessLayer.Abstract.ILogDal import ILogDal
from EntityLayer.Concrete.Log import Log

# LogManager sınıfı ILogService interface'inden miras alır.
# ILogService interface'inde tanımlı olan metodları bu sınıf içerisinde implemente ederiz
# ve bu metodları kullanarak işlemlerimizi gerçekleştiririz

class LogManager(ILogService):
    
    def __init__(self, logDal: ILogDal) -> None:
        self.logDal = logDal

    # Log ekleme işlemi sağlayan metot.
    def TAdd(self, log: Log) -> None:
        query = "INSERT INTO logs (LogMessage, LogDate, UserID) VALUES (%s, %s, %s)"
        params = (log.LogMessage, log.LogDate, log.UserID)
        self.logDal.Insert(query, params)