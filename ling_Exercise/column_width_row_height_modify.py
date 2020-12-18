import openpyxl

work_book = openpyxl.load_workbook("C://Users//baozipu//Desktop//sum.xlsx")
sheet = work_book.get_sheet_by_name("合计")


def row_height_modify(row,height):
    sheet.row_dimensions[row].height = height

def column_width_modify(column,width):
    sheet.column_dimensions[column].width = width

def row_hidden(row):
    sheet.row_dimensions[row].hidden = 1

def column_hidden(column):
    sheet.column_dimensions[column].hidden = 1

def row_unhidden(row):
    sheet.row_dimensions[row].hidden = 0

def column_unhidden(column):
    sheet.column_dimensions[column].hidden = 0


work_book.save("C://Users//baozipu//Desktop//sum.xlsx")