import openpyxl
from exceltools import ExcelTools


if __name__ == '__main__':
    excel_tools = ExcelTools()
    file_reader = excel_tools.createFileReader("C://Users//peigen//Desktop//刷题本.xlsx")
    sheet_names = file_reader.get_sheetnames()
    print(file_reader.get_sheetnames())
    for sheetName in sheet_names:
        print(sheetName + ":")
        print(file_reader.sum_by_rows(sheetName , "A1"))
 
    