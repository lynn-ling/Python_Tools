import openpyxl

class excel_reader():
    def __init__(self):
        pass

    def file_reader(self, filePath):
        return file_reader(filePath)


class file_reader():
    def __init__(self, filePath):
        self.filePath = filePath
        self.workbook = openpyxl.load_workbook(filePath)
        pass

    def get_workbook(self):
        return self.workbook.get_sheet_names()

    def get_sheetnames(self):
        return self.workbook.get_sheet_names()


    def sum_by_rows(self, sheetName, rows):
        sheet = self.workbook.get_sheet_by_name(sheetName)
       


    def sumBycolum(self,sheetName, column):
        #todo
        pass
        

``