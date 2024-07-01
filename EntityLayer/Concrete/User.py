from typing import Optional
import datetime

# Kullanıcı model sınıfı, kullanıcı işlemleri için kullanılır.
class User:
    Id: Optional[int]
    Number: str
    Username: str
    Password: str
    Name: str
    Surname: str
    CreatedDate: Optional[datetime.datetime]

    def __init__(self, Number: str, Username: str, Password: str, Name: str, Surname: str, CreatedDate: Optional[datetime.datetime] = None, Id: Optional[int] = None):
        self.Id = Id
        self.Number = Number
        self.Username = Username
        self.Password = Password
        self.Name = Name
        self.Surname = Surname
        self.CreatedDate = CreatedDate
