from workbook import ExcelWorkbook
ew=ExcelWorkbook("sample.xlsx")
ew.write("A2",123)
ew.write("B1","hello")
ew.append([123,568])