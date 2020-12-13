import openpyxl
from exceltools import ExcelTools


if __name__ == '__main__':
    excel_tools = ExcelTools()
    file_reader = excel_tools.createFileReader("C://Users//peigen//Desktop//刷题本.xlsx")
    print(file_reader.getSheetNames())
    