import openpyxl
from read.readertools import excel_reader,file_reader
#from write.writertools import excel_writer,file_writer

class ExcelTools():
    def __init__(self):
        pass

    def createFileReader(self, filePath):
        return excel_reader().file_reader(filePath)

    def createFileWriter(self, filePath):
        return excel_writer().file_writer(filePath)