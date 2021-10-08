import openpyxl
import pandas as pd

filein = 'D:\\GIT\\Files\\cpamexport\\export.xlsx'   
wb = openpyxl.load_workbook(filein)
ws = wb['Лист1']
i = 2
row = ws.max_row + 1
ws.cell(row=1, column=9).value = 'Personnel Type'
ws.cell(row=1, column=10).value = 'Access Level'
ws.cell(row=1, column=11).value = 'Badge Format'
ws.cell(row=1, column=12).value = 'Badge Type'
while i != row:
    photo = ws.cell(row=i, column=6).value
    ws.cell(row=i, column=6).value = 'D:\\GIT\\Files\\photo\\' + photo
    if ws.cell(row=i, column=5).value == ' ':
        ws.cell(row=i, column=9).value = 'Student'
    else:
        ws.cell(row=i, column=9).value = 'Employee - Full Time'
    ws.cell(row=i, column=10).value = 'All turnstile'
    ws.cell(row=i, column=11).value = '34bit_noFAC'
    ws.cell(row=i, column=12).value = 'Standard'
    i += 1


wb.save(filename = filein)
data_xls = pd.read_excel(filein, dtype=str, index_col=None)
data_xls.to_csv('d:\\git\\files\\export.csv', encoding='cp1251', index=False)



