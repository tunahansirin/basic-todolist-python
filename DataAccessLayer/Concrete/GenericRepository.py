from typing import List, TypeVar, Optional, Type, Generic
from DataAccessLayer.Abstract.IGenericDal import IGenericDal
from DataAccessLayer.Context import DBContext
import inspect

# Burada sınıfın Generic olduğunu belirtmek için Generic sınıfını miras aldık.
T = TypeVar('T')

# GenericRepository sınıfı, veritabanı işlemlerinin yapıldığı sınıf
class GenericRepository(IGenericDal[T], Generic[T]):

    def __init__(self, entity_type: Type[T]) -> None:
        self.entity_type = entity_type

    # Veri tabanındaki veriyi güncellemek için kullanılan metot.
    def Update(self, query: str, params: tuple) -> None:

        # Burada tanımlanmasının amacı finnally bloğunda cursor ve connection nesnelerini kapatmaktır.        
        connection = None
        cursor = None

        try:
            # Burada veritabanı bağlantısı alınmaktadır.
            connection = DBContext.GetConnect()

            # Eğer bağlantı alındıysa işlem yapılabilir.
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()

        finally:
            # Burada cursor ve connection nesneleri kapatılmaktadır.
            cursor.close()
            connection.close()

    # Veri eklemek için kullanılan metot.
    def Insert(self, query: str, params: tuple) -> None:
        connection = DBContext.GetConnect()

        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()

            finally:
                cursor.close()
                connection.close()

    
    # Birden fazla veri eklemek için kullanılan metot.
    def InsertRange(self, query: str, params_list: List[tuple]) -> None:
        connection = DBContext.GetConnect()

        if connection:
            try:
                cursor = connection.cursor()
                cursor.executemany(query, params_list)
                connection.commit()

            finally:
                cursor.close()
                connection.close()

    # Veri silmek için kullanılan metot.
    def Delete(self, query: str, params: tuple) -> None:
        connection = DBContext.GetConnect()

        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()

            finally:
                cursor.close()
                connection.close()
    
    # Birden fazla veriyi silmek için kullanılan metot.
    def DeleteRange(self, query: str, params_list: List[tuple]) -> None:
        connection = DBContext.GetConnect()

        if connection:
            try:
                cursor = connection.cursor()
                cursor.executemany(query, params_list)
                connection.commit()

            finally:
                cursor.close()
                connection.close()

    # Veri getirmek için kullanılan metot.
    def GetByFilter(self, query: str, params: tuple) -> Optional[T]:
        connection = DBContext.GetConnect()
        entity = None

        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, params)
                result = cursor.fetchone()

                # Burada geriye döndürürken tanımlanmış sınıflara uygun hale getirmek için işlem yapılmaktadır. 
                # Örnek veriyorum ben user ile ilgili bir veri getireceksem bu verinin user modeline uygun şekilde geriye dönmesini sağlamaktayım.
                if result:
                    # entity_type sınıfının __init__ metodunun parametre isimlerini al
                    init_params = inspect.signature(self.entity_type.__init__).parameters

                    # Parametre isimleri listesinden 'self'i çıkar
                    init_params = [param for param in init_params if param != 'self']

                    # Sonuç sözlüğünü, sadece init_params içinde bulunan anahtarları içerecek şekilde filtrele
                    filtered_result = {k: v for k, v in result.items() if k in init_params}

                    # Filtrelenmiş sonuç sözlüğünü argüman olarak kullanarak entity_type sınıfının bir örneğini oluştur
                    entity = self.entity_type(**filtered_result)

            finally:
                cursor.close()
                connection.close()

        return entity
    
    # Birden fazla veriyi getirmek için kullanılan metot.
    def GetListByFilter(self, query: str, params: tuple) -> List[T]:
        connection = DBContext.GetConnect()
        entities = []

        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, params)
                results = cursor.fetchall()

                if results:
                    init_params = inspect.signature(self.entity_type.__init__).parameters
                    init_params = [param for param in init_params if param != 'self']

                    for result in results:
                        filtered_result = {k: v for k, v in result.items() if k in init_params}
                        entity = self.entity_type(**filtered_result)
                        entities.append(entity)

            finally:
                cursor.close()
                connection.close()

        return entities
