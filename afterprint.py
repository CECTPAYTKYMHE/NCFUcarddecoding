import openpyxl
import pandas as pd

filein = 'D:\\GIT\\card\\2001-2272.xlsx'   
wb = openpyxl.load_workbook(filein)
ws = wb['Лист1']
i = 2
row = ws.max_row + 1
ws.cell(row=1, column=6).value = 'Personnel Type'
ws.cell(row=1, column=8).value = 'Access Level'
ws.cell(row=1, column=9).value = 'Badge Format'
ws.cell(row=1, column=10).value = 'Badge Type'
while i != row:
    photo = ws.cell(row=i, column=5).value
    ws.cell(row=i, column=5).value = 'D:\\GIT\\card\\photo\\' + photo
    ws.cell(row=i, column=6).value = 'Employee - Full Time'
    ws.cell(row=i, column=8).value = 'All turnstile'
    ws.cell(row=i, column=9).value = '34bit_noFAC'
    ws.cell(row=i, column=10).value = 'Standard'
    i += 1


wb.save(filename = filein)
data_xls = pd.read_excel(filein, dtype=str, index_col=None)
data_xls.to_csv('d:\\git\\card\\tocpam5.csv', encoding='cp1251', index=False)



