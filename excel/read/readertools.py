import openpyxl


class file_reader():
    def __init__(self, filePath):
        self.filePath = filePath
        self.workbook = openpyxl.load_workbook(filePath)
        pass

    def getSheetNames(self):
        return self.workbook.get_sheet_names()

    def getAllCellsBySheets(self,sheetName):
        self.workbook.get_sheet_by_name(sheetName)
        return 

class excel_reader():
    def __init__(self):
        pass

    def file_reader(self, filePath):
        return file_reader(filePath)