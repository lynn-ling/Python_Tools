import openpyxl
import pprint

open_file = openpyxl.load_workbook("C://Users//baozipu//Desktop//automate_online-materials//censuspopdata.xlsx")
sheet = open_file.get_sheet_by_name("Population by Census Tract")

country_census = {}

for cell in range(2, sheet.max_row+1):
    state = sheet["B"+str(cell)].value
    country = sheet["C"+str(cell)].value
    pop = sheet["D"+str(cell)].value

    country_census.setdefault(state,{})
    country_census[state].setdefault(country,{"tracts":0,"pop":0})

    country_census[state][country]["tracts"]+=1
    country_census[state][country]["pop"]+=int(pop)

result_file = open("population_result.py","w")
result_file.write(pprint.pformat(country_census))
result_file.close()



