import openpyxl

work_book = openpyxl.load_workbook("C://Users//baozipu//Desktop//sum.xlsx")
sheet = work_book.get_sheet_by_name("合计")

row_num1 = 1
row_num2 = 5
column_num1 = "A"
column_num2 = "B"

sheet.row_dimensions[row_num1].height = 70
sheet.row_dimensions[row_num2].hidden = 1
sheet.column_dimensions[column_num1].width = 20
sheet.column_dimensions[column_num2].hidden = 0

work_book.save("C://Users//baozipu//Desktop//sum.xlsx")