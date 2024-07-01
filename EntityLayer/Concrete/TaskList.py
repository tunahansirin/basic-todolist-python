from typing import Optional
import datetime

# TaskList model sınıfı, görev listesi işlemleri için kullanılır.
class TaskList:
    Id: Optional[int]
    ListName: str
    CreatedDate: datetime.datetime
    UserID: int

    def __init__(self, ListName: str, CreatedDate: datetime.datetime, UserID: int, Id: Optional[int] = None):
        self.Id = Id
        self.ListName = ListName
        self.CreatedDate = CreatedDate
        self.UserID = UserID