import openpyxl
from openpyxl_image_loader import SheetImageLoader
import os
import csv
from PIL import Image
cwd = os.path.abspath('D:\\GIT\\Files\\student\\2 курс очная форма')
files = os.listdir(cwd)
Image.MAX_IMAGE_PIXELS = None
logs = open(f'D:\\GIT\\Files\\student\\errorlogs{cwd[21:22]}.csv', 'w')
logs.write('Ошибка фотографии в файле, Строка, ФИО\n')
logs.close()
for file in files:
    try:
        filein = cwd + '\\' + file
        wb = openpyxl.load_workbook(filein)
        ws = wb['ФИОиФото']
        i = 3 #начальная строка
        row = ws.max_row
        image_loader = SheetImageLoader(ws)
        ws.cell(row=1, column=1).value = 'ID'
        ws.cell(row=1, column=2).value = 'Фамилия'
        ws.cell(row=1, column=3).value = 'Имя'
        ws.cell(row=1, column=4).value = 'Отчество'
        ws.cell(row=1, column=5).value = 'Фотография №'
        ws.cell(row=1, column=6).value = 'Role'
        while i != row + 1: #проверить конечную строку!!!!
            ID = ws.cell(row=i, column=1)
            ID = str(ID.value)
            ID = ID.replace('-','')
            ID = ID.upper()
            try:
                ws.unmerge_cells(start_row=i, start_column=5, end_row=i, end_column=6)
            except:
                pass
            try:
                image = image_loader.get('E' + str(i)) #клетка с фотографией
                image.save('d:\\git\\files\\student\\photo\\' + ID + '.jpg') #экспорт фото
                ws.cell(row=i, column=5).value = ID + '.jpg' #имяфото.jpg
            except:
                logs = open(f'D:\\GIT\\Files\\student\\errorlogs{cwd[21:22]}.csv','a')
                print(f'<Неправильная фотография в файле {cwd[21:]}\{file} в строке {i-1} у студента {ws.cell(row=i, column=2).value} {ws.cell(row=i, column=3).value} {ws.cell(row=i, column=4).value}>')
                logs.write(f'{cwd[21:]}\\{file}, {i-1}, {ws.cell(row=i, column=2).value} {ws.cell(row=i, column=3).value} {ws.cell(row=i, column=4).value} \n')
                logs.close()
                pass
            ws.cell(row=i-1, column=6).value = 'Student'
            ws.cell(row=i, column=1).value = ID #удаление '-' в NCFUGUID
            ws.cell(row=i-1, column=1).value = ws.cell(row=i, column=1).value
            ws.cell(row=i-1, column=2).value = ws.cell(row=i, column=2).value
            ws.cell(row=i-1, column=3).value = ws.cell(row=i, column=3).value
            ws.cell(row=i-1, column=4).value = ws.cell(row=i, column=4).value
            ws.cell(row=i-1, column=5).value = ws.cell(row=i, column=5).value
            i += 1
        ws.delete_rows(row)
        ws._images = [] # удаление всех фото из файла
        #ws.delete_cols(7, 2) # удаление столбцов с 7 по 9(7 + 2)
        wb.save(filename = filein)
        print(f'{file} успех')
    except:
        print(f'{file} в строке {i} завершился неудачно')

