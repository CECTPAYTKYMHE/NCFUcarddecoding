import openpyxl
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader

#filein = input('Полный путь до файла > ') 
filein = 'D:\\GIT\\Files\\cpamexport\\student.xlsx'
wb = openpyxl.load_workbook('D:\\GIT\\Files\\cpamexport\\student.xlsx')
ws = wb['Лист1']


i = 3
row = ws.max_row
image_loader = SheetImageLoader(ws)
while i != row + 1:
    ID = ws.cell(row=i, column=1)
    ID = str(ID.value)
    ID = ID.replace('-','')
    image = image_loader.get('E' + str(i))
    image.save('d:\\git\\files\\photo\\' + ID + '.jpg')
    ws.cell(row=i, column=5).value = ID +'.jpg'
    i += 1
ws._images = []
wb.save(filename = filein)

