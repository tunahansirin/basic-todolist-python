import mysql.connector

# Veritabanı bağlantısı için gerekli olan bilgilerin tanımlandığı sınıf
class DBContext:

    # Statik metotlar ile veritabanı bilgilerinin geri döndürüldüğü sınıf
    @staticmethod
    def GetConnect():
        connection = mysql.connector.connect(
            host='localhost',
            database='srntodolistdb',
            user='root',
            password=''
        )
        return connection
