from typing import Optional
import datetime


# Task model sınıfı, görev nesneleri işlemleri için kullanılır.
class Task:
    Id: Optional[int]
    TaskName: str
    Status: int
    CompletedDate: Optional[datetime.date]
    ListID: int

    def __init__(self, TaskName: str, Status: int, CompletedDate: Optional[datetime.date], ListID: int, Id: Optional[int] = None):
        self.Id = Id
        self.TaskName = TaskName
        self.Status = Status
        self.CompletedDate = CompletedDate
        self.ListID = ListID
