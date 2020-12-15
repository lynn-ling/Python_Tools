import openpyxl
from exceltools import ExcelTools


if __name__ == '__main__':
    excel_tools = ExcelTools()
    file_reader = excel_tools.createFileReader("C://Users//baozipu//Desktop//sum.xlsx")
    sheet_names = file_reader.get_sheetnames()
    print(file_reader.content_cells_range("合计"))


    #file_wirter = excel_tools.createFileWriter("C://Users//peigen//Desktop//hello.xlsx")
    #sheet = file_wirter.create_sheet("你好")


    #file_wirter.add_data(sheet,[["ab","cd"],["ef","hi"]])
    #file_wirter.save()
    
    # for sheetName in sheet_names:
    #     print(file_reader.sum_by_column("合计" , "B"))
 
    