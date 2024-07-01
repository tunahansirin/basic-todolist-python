from DataAccessLayer.Abstract.IUserDal import IUserDal
from DataAccessLayer.Concrete.GenericRepository import GenericRepository
from EntityLayer.Concrete.User import User

# User verilerinin veritabanı işlemlerinin yapıldığı sınıf
class UserRepository(GenericRepository[User], IUserDal):

    # Burada GenericRepository sınıfından miras alınarak User verilerinin veritabanı işlemleri yapılmıştır.
    def __init__(self):
        super().__init__(User)
