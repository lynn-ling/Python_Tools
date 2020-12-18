import openpyxl


work_book = openpyxl.load_workbook("C://Users//baozipu//Desktop//sum.xlsx")
sheet = work_book.get_sheet_by_name("合计")

def cell_freeze(cell):
    sheet.freeze_panes = cell
    work_book.save("C://Users//baozipu//Desktop//sum.xlsx")



def cell_unfreeze(cell):
    sheet.freeze_panes = None
    work_book.save("C://Users//baozipu//Desktop//sum.xlsx")

cell_unfreeze("B2")