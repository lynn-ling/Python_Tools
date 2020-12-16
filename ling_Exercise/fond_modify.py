import openpyxl
from openpyxl.styles import Font

work_sheet = openpyxl.load_workbook("C://Users//baozipu//Desktop//sum.xlsx")
sheet = work_sheet.get_sheet_by_name("合计")
fontObj=Font(bold=True)
cell_range = sheet["A2":"B10"]
for tuples in cell_range:
    for cells in tuples:
        cells.font = fontObj

work_sheet.save("C://Users//baozipu//Desktop//sum.xlsx")

