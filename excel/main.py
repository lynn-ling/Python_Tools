import openpyxl
from exceltools import ExcelTools


if __name__ == '__main__':
    excel_tools = ExcelTools()
    file_reader = excel_tools.createFileReader("C://Users//baozipu//Desktop//sum.xlsx")
    sheet_names = file_reader.get_sheetnames()
    for sheetName in sheet_names:
        print(file_reader.sum_by_column(sheetName , "A1"))
 
    