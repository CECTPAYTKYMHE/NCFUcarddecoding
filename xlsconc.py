import os
import pandas as pd
cwd = os.path.abspath('D:\\GIT\\card')
files = os.listdir(cwd)
filesdata = []
for file in files:
    print(file)
    k = pd.read_excel(cwd + '\\' + file)
    filesdata.append(k)



appended_xlsx = pd.concat(filesdata)

appended_xlsx.to_excel('D:\\GIT\\card\\allemployee.xlsx', index=False)