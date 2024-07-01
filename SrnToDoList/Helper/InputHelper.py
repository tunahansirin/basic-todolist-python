from SrnToDoList.Helper.ClearHelper import ClearHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

# InputHelper sınıfında kullanıcıdan veri almak için gerekli olan metotlar bulunmaktadır.
class InputHelper:
    def __init__(self):
        self.writerHelper = WriterHelper()
        self.clearHelper = ClearHelper()

    # getInputControl metodu, kullanıcıdan veri almak için kullanılır. Girilen veri, validationFunction metodu ile kontrol edilir.
    def getInputControl(self, text,goPage, validationFunction=None):
        while True:
            try:
                value = self.writerHelper.writerText(text, prompt=True)
                
                goPage() if value == '0' else None

                validationFunction(value) if validationFunction is not None else None

                return value
            
            except ValueError as e:
                self.clearHelper.ClearLastLines(1)
                self.writerHelper.writerText(str(e), color="error")