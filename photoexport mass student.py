import openpyxl
from openpyxl_image_loader import SheetImageLoader
import os
cwd = os.path.abspath('D:\\GIT\\Files\\student\\2 курс очная форма')
files = os.listdir(cwd)

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
       #ws.cell(row=1, column=7).value = ''
        while i != row + 1: #проверить конечную строку!!!!
            ID = ws.cell(row=i, column=1)
            ID = str(ID.value)
            ID = ID.replace('-','')
            ID = ID.upper()
            ws.unmerge_cells(start_row=i, start_column=5, end_row=i, end_column=6)
            try:
                image = image_loader.get('E' + str(i)) #клетка с фотографией
                image.save('d:\\git\\files\\student\\photo\\' + ID + '.jpg') #экспорт фото
                ws.cell(row=i, column=5).value = ID + '.jpg' #имяфото.jpg
            except:
                logs = open('D:\\GIT\\Files\\student\\errorlogs.txt', 'a')
                print(f'<Неправильная фотография в файле {cwd[21:]}\{file} в строке {str(i)} у студента {ws.cell(row=i, column=2).value} {ws.cell(row=i, column=3).value} {ws.cell(row=i, column=4).value}>')
                logs.write(f'<Неправильная фотография в файле {cwd[21:]}{file} в строке {str(i)} у студента {ws.cell(row=i, column=2).value} {ws.cell(row=i, column=3).value} {ws.cell(row=i, column=4).value}>\n')
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

