import os

# ClearHelper sınıfında konsol ekranını temizlemek için gerekli olan metotlar bulunmaktadır.
class ClearHelper:

    # Konsol ekranının tamamını temizlemek için ClearConsole metodu kullanılır.    
    def ClearConsole(self):
        os.system('cls')

    # Konsol ekranının sadece belirli bir kısmını temizlemek için ClearLastLines metodu kullanılır.
    # count değeri kaç satır temizleneceğini belirtir.
    def ClearLastLines(self, count):
        CursorUpOne = '\x1b[1A'
        EraseLine = '\x1b[2K'
        
        for i in range(count):
            print(CursorUpOne + EraseLine + CursorUpOne)
