import os
import pandas as pd
import glob
import openpyxl
cwd = 'D:\\GIT\\Files\\выгрузки\\241221\\готовое\\rej\\'
files = [f for f in glob.glob(cwd + '**/*.xlsx', recursive=True)]
filesdata = []
for file in files:
    wb = openpyxl.load_workbook(file)
    ws = wb.worksheets[0]
    ws._images = []
   # ws.delete_rows(1)
    wb.save(filename = file)
    wb.close()
    print(file)
    k = pd.read_excel(file)
    filesdata.append(k)



appended_xlsx = pd.concat(filesdata)

appended_xlsx.to_excel('D:\\GIT\\Files\\выгрузки\\241221\\готовое\\rej\\rej.xlsx', index=False)
