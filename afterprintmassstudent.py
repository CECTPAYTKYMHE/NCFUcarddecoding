import openpyxl
import pandas as pd
import glob
cwd = 'D:\\GIT\\Files\\photo\\toexport'
files = [f for f in glob.glob(cwd + '**/*.xlsx', recursive=True)]
id = 0
for file in files:
    id += 1
    wb = openpyxl.load_workbook(file)
    ws = wb['Лист1']
    ws.insert_rows(1)
    i = 2
    row = ws.max_row + 1
    ws.cell(row=1, column=1).value = 'Personnel ID'
    ws.cell(row=1, column=2).value = 'Last Name'
    ws.cell(row=1, column=3).value = 'First Name'
    ws.cell(row=1, column=4).value = 'Middle Name'
    ws.cell(row=1, column=5).value = 'Photo'
    ws.cell(row=1, column=6).value = 'Personnel Type'
    ws.cell(row=1, column=7).value = 'Card #'
    ws.cell(row=1, column=8).value = 'Access Level'
    ws.cell(row=1, column=9).value = 'Badge Format'
    ws.cell(row=1, column=10).value = 'Badge Type'
    while i != row:
        photo = ws.cell(row=i, column=5).value
        
      #  if ws.cell(row = i, column=7).value == None:
       #     print(f"yes {i}")
        try:
            cardid = ws.cell(row=i, column=7).value
            ws.cell(row=i, column=7).value = int(cardid)
        except:
            log = open('D:\\GIT\\Files\\photo\\toexport\\logs.txt', 'a')
            log.write(f'Отсутствует номер карты в файле {file} в строке {i}\n')
            log.close()
        ws.cell(row=i, column=5).value = 'D:\\GIT\\files\\photo\\student\\' + photo
        ws.cell(row=i, column=6).value = 'Student'
        ws.cell(row=i, column=8).value = 'All turnstile'
        ws.cell(row=i, column=9).value = '34bit_noFAC'
        ws.cell(row=i, column=10).value = 'Standard'
        i += 1
    wb.save(filename = file)
    data_xls = pd.read_excel(file, dtype=str, index_col=None)
    data_xls.to_csv(f'D:\\GIT\\Files\\photo\\toexport\\{id}.csv', encoding='cp1251', index=False)



