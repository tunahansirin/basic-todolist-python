import random
from BusinessLayer.Concrete.UserManager import UserManager
from DataAccessLayer.Concrete.UserRepository import UserRepository

# GenericCode sınıfı, kullanıcı numarası oluşturmak için gerekli olan metotları içerir.
class GenericCode: 

    def __init__(self):
        self.userManager = UserManager(UserRepository())

    # GenericCodeNumber metodu, kullanıcı numarası oluşturmak için kullanılır.
    def GenericCodeNumber(self):
        numberList = '1234567890'
        resultNumber = ""

        for i in range(11):
            resultNumber += random.choice(numberList)

        return resultNumber
    
    
    # GenericCodeNumber metodundan üretilen numaranın veritabanında olup olmadığını kontrol eder. Eğer numara veritabanında yoksa numarayı döndürür
    def GenericCodeNumberDB(self):
        while True:
            number = self.GenericCodeNumber()
            if self.userManager.GetByNumber(number) is None:
                return number