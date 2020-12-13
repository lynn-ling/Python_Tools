import openpyxl
from read.readertools import excel_reader,file_reader

class ExcelTools():
    def __init__(self):
        pass

    def createFileReader(self, filePath):
        return excel_reader().file_reader(filePath)

