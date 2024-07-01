from typing import Optional
import datetime

# Log model sınıfı, log işlemleri için kullanılır. Genel olarak bir şablon oluşturulmuştur.
class Log:
    Id: Optional[int]
    LogMessage: str
    LogDate: datetime.datetime
    UserID: int

    def __init__(self, 
                 LogMessage: str, 
                 UserID: int, 
                 LogDate: Optional[datetime.datetime] = None, 
                 Id: Optional[int] = None):
        self.Id = Id
        self.LogMessage = LogMessage
        self.UserID = UserID
        self.LogDate = LogDate if LogDate is not None else datetime.datetime.now()