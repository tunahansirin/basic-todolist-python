from typing import Optional

# Kullanıcı Kayıt Modeli, kullanıcı kayıt işlemi için kullanılır.
class UserRegisterModel:
    Username: str
    Password: str
    Name: str
    Surname: str
    
    def __init__(self, Username, Password, Name, Surname):
        self.Username = Username
        self.Password = Password
        self.Name = Name
        self.Surname = Surname