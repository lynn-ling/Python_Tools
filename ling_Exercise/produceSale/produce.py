import openpyxl

work_book = openpyxl.load_workbook("C://Github//Python_Tools//ling_Exercise//produceSale//produceSales.xlsx")
sheet = work_book.get_sheet_by_name("Sheet")

price_update = {
    "Garlic":3.07,
    "Celery":1.19,
    "Lemon":1.27
}

for rowNum in range(2,sheet.max_row+1):
    content_value = sheet["A"+str(rowNum)].value
    if  content_value in price_update:
        sheet["B"+str(rowNum)] = price_update[content_value]

work_book.save("C://Github//Python_Tools//ling_Exercise//produceSale//after_update_produceSale.xlsx")