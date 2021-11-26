import xlrd

filePath = "/home/christian/Downloads/Entretenimiento.xlsx"

openFile =xlrd.open_workbook(filePath)

sheet =openFile.sheet_by_name('Entretenimiento')

print(sheet.rows)