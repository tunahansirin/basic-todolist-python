import time
import pandas as pd
import os
from BusinessLayer.Validator.TaskListValidator import TaskListValidator
from BusinessLayer.Validator.TaskValidator import TaskValidator
from SrnToDoList.Helper.UserHelper import UserHelper
from SrnToDoList.Helper.WriterHelper import WriterHelper

class FileHelper:
    def __init__(self, filePath):
        self.filePath = filePath
        self.df = None
        self.taskColumns = []
        self.dfLong = None
        self.writeHelper = WriterHelper()

    # LoadExcel metodu, dosyayı okur ve veriyi yükler.
    def LoadExcel(self):
        if not self.filePath.endswith(('.xls', '.xlsx')):
            raise ValueError("Dosya uzantısı .xls veya .xlsx olmalıdır.")
        
        if not os.path.exists(self.filePath):
            raise FileNotFoundError(f"Dosya bulunamadı: {self.filePath}")
        
        self.df = pd.read_excel(self.filePath)

    # FindListNameColumn metodu, ListName sütununun olup olmadığını kontrol eder.  
    def FindListNameColumn(self):
        if 'ListName' not in self.df.columns:
            raise ValueError("ListName sütunu bulunamadı.")

    # FindTaskColumns metodu, TaskName ile başlayan sütunları bulur.
    def FindTaskColumns(self):
        self.taskColumns = [col for col in self.df.columns if col.startswith('TaskName')]
        if not self.taskColumns:
            raise ValueError("TaskName ile başlayan geçerli bir sütun bulunamadı.")
    
    # CheckListName metodu, ListName'in geçerli olup olmadığını kontrol eder.
    def CheckListName(self, listName:str, userID: int) -> None:
        taskListrValidator = TaskListValidator(userID=userID)
        taskListrValidator.ValidateListName(listName)
        
    # CheckTaskName metodu, TaskName'in geçerli olup olmadığını kontrol eder.
    def CheckTaskName(self, taskNmaeList: list[str]) -> None:
        taskValidator = TaskValidator()
        taskValidator.ValidateTaskUnique(taskNmaeList)
        taskValidator.ValidateTaskCount(len(taskNmaeList))

    # MeltDataFrame metodu, veriyi düzenler.
    def MeltDataFrame(self):
        self.dfLong = self.df.melt(id_vars=['ListName'], value_vars=self.taskColumns, var_name='Task', value_name='TaskValue')

    # DropNan metodu, NaN değerleri düşürür.
    def DropNan(self):
        self.dfLong = self.dfLong.dropna(subset=['TaskValue'])

    # GetListNameTaskContents metodu, ListName ve TaskValue değerlerini birleştirir.
    def GetListNameTaskContents(self):
        return self.dfLong.groupby('ListName')['TaskValue'].apply(list).to_dict()

    # ProcessFile metodu, dosyayı işler ve verileri döndürür. Gerekli koşullar sağlanmazsa hata döndürür.
    def ProcessFile(self, userID: int):
        try:
            self.LoadExcel()
            self.FindListNameColumn()
            self.FindTaskColumns()
            self.MeltDataFrame()
            self.DropNan()

            taskList = self.GetListNameTaskContents()

            for listName, taskNameList in taskList.items():
                self.CheckListName(listName, userID)
                self.CheckTaskName(taskNameList)

            return taskList
        
        except ValueError as error:
            self.writeHelper.writerText(str(error), color="error")
            self.writeHelper.writerText(" Dosya işleme başarısız oldu. Lütfen gerekli koşulları sağlayıp tekrar deneyiniz.", color="error")
            time.sleep(3)
            return None
        
        except FileNotFoundError as error:
            self.writeHelper.writerText(str(error), color="error")
            self.writeHelper.writerText(" Dosya işleme başarısız oldu. Lütfen gerekli koşulları sağlayıp tekrar deneyiniz.", color="error")
            time.sleep(3)
            return None