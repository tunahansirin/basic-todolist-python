from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.UserRepository import UserRepository

# TaskListValidator sınıfı, kullanıcıyla ilgili bilgilerin doğruluğunu kontrol eder.
class UserValidator:

    def __init__(self) -> None:
        self.userManager = UserManager(UserRepository())

    # Kullanıcı adının istenilen kuralları sağlayıp sağlamadığını kontrol eden metot.
    def ValidateUsername(self, username: str):
        if not username:
            raise ValueError("Kullanıcı adı boş olamaz")
        
        if len(username) < 3:
            raise ValueError("Kullanıcı adı en az 3 karakter uzunluğunda olmalıdır")
        
        if self.userManager.GetByUsername(username) is not None:
            raise ValueError("Kullanıcı adı zaten mevcut. Lütfen başka bir kullanıcı adı girin")
    
    # Şifrenin istenilen kuralları sağlayıp sağlamadığını kontrol eden metot.
    def ValidatePassword(self, password: str):
        if not password:
            raise ValueError("Şifre boş olamaz")
        
        if len(password) < 6:
            raise ValueError("Şifre en az 6 karakter uzunluğunda olmalıdır")

    # Adın istenilen kuralları sağlayıp sağlamadığını kontrol eden metot.
    def ValidateName(self, name: str):
        if not name:
            raise ValueError("Ad boş olamaz")

    # Soyadın istenilen kuralları sağlayıp sağlamadığını kontrol eden metot.
    def ValidateSurname(self, surname: str):
        if not surname:
            raise ValueError("Soyad boş olamaz")