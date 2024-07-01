from DataAccessLayer.Abstract.ILogDal import ILogDal
from DataAccessLayer.Concrete.GenericRepository import GenericRepository
from EntityLayer.Concrete.Log import Log

# Log verilerinin veritabanı işlemlerinin yapıldığı sınıf
class LogRepository(GenericRepository[Log], ILogDal):

    # Burada GenericRepository sınıfından miras alınarak Log verilerinin veritabanı işlemleri yapılmıştır.
    def __init__(self):
        super().__init__(Log)