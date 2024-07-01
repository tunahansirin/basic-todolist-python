from typing import Optional
from BusinessLayer.Abstract.IUserService import IUserService
from DataAccessLayer.Abstract.IUserDal import IUserDal
from EntityLayer.Concrete.User import User

# UserManager sınıfı IUserService interface'inden miras alır.
# IUserService interface'inde tanımlı olan metodları bu sınıf içerisinde implemente ederiz
# ve bu metodları kullanarak işlemlerimizi gerçekleştiririz

class UserManager(IUserService):

    def __init__(self, user_dal: IUserDal):
        self.user_dal = user_dal

    # Kullanıcı eklememizi sağlayan metot.
    def TAdd(self, user: User) -> None:
        query = "INSERT INTO Users (Number, Username, Password, Name, Surname, CreatedDate) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (user.Number, user.Username, user.Password, user.Name, user.Surname, user.CreatedDate)
        self.user_dal.Insert(query, params)

    # Kullanıcı adına göre Kullanıcı getiren metot.
    def GetByUsername(self, username: str) -> Optional[User]:
        query = "SELECT * FROM Users WHERE Username = %s"
        params = (username,)
        return self.user_dal.GetByFilter(query, params)

    # Kullanıcı numarasına göre kullanıcı getiren metot.
    def GetByNumber(self, number: str) -> Optional[User]:
        query = "SELECT * FROM Users WHERE Number = %s"
        params = (number,)
        return self.user_dal.GetByFilter(query, params)

    # Kullanıcının şifresini kontrol etmemizi sağlayan metot.
    def GetByUsernameAndPassword(self, username: str, password: str) -> Optional[User]:
        query = "SELECT * FROM Users WHERE Username = %s AND Password = %s"
        params = (username, password)
        return self.user_dal.GetByFilter(query, params)
    
    # Kullanıcın bilgilerini güncelleyen metot.
    def UpdateUserAbout(self, userID: int, name: str, surname:str) -> None:
        query = "UPDATE Users SET Name = %s, Surname = %s WHERE Id = %s"
        params = (name, surname, userID)
        self.user_dal.Update(query, params)

    # Kullanıcının şifresini güncelleyen metot.
    def UpdateUserPassword(self, userID: int, password: str) -> None:
        query = "UPDATE Users SET Password = %s WHERE Id = %s"
        params = (password, userID)
        self.user_dal.Update(query, params)