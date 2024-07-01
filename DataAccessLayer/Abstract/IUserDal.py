from abc import ABC
from EntityLayer.Concrete.User import User
from DataAccessLayer.Abstract.IGenericDal import IGenericDal

# Generic interface'ini miras alarak Log nesnesi için CRUD işlemleri tanımlıyoruz.
class IUserDal(IGenericDal[User], ABC):
    pass
