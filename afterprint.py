import openpyxl
import pandas as pd

filein = 'D:\\GIT\\files\\выгрузки\\071221\\+Сотрудники.xlsx'   
wb = openpyxl.load_workbook(filein)
ws = wb['Sheet1']
i = 2
row = ws.max_row + 1
ws.cell(row=1, column=6).value = 'Personnel Type'
ws.cell(row=1, column=8).value = 'Access Level'
ws.cell(row=1, column=9).value = 'Badge Format'
ws.cell(row=1, column=10).value = 'Badge Type'
ws.cell(row=1, column=11).value = 'Watch level'
while i != row:
    photo = ws.cell(row=i, column=5).value
    ws.cell(row=i, column=5).value = 'D:\\GIT\\files\\photo\\employee\\' + photo
    ws.cell(row=i, column=6).value = 'Employee - Full Time'
    ws.cell(row=i, column=8).value = 'All turnstile'
    ws.cell(row=i, column=9).value = '34bit_noFAC'
    ws.cell(row=i, column=10).value = 'Standard'
    ws.cell(row=i, column=11).value = 'Сотрудники'
    i += 1


wb.save(filename = filein)
data_xls = pd.read_excel(filein, dtype=str, index_col=None)
data_xls.to_csv('d:\\git\\files\\выгрузки\\071221\\employee0712.csv', encoding='cp1251', index=False)



