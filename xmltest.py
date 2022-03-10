import xmltodict
import ast
import json
from collections import defaultdict
data = []
def getkey(xml):
    return xml.keys()

def getdata(i, nomch = '-', dataoper = 0, naznpl = 0, naimpp = 0, inn = 0):
    if '@НомКорСч' in i['РеквБанка']:
        nomch = i['РеквБанка']['@НомКорСч']
    dataoper = i['@ДатаОпер']
    naznpl = i['@НазнПл']
    naimpp = i['РеквПлат']['@НаимПП']
    inn = i['РеквПлат']['@ИННПП']
    return (nomch,dataoper,naznpl,naimpp,inn)

with open('c:/git/xml/19292/BVD1_ZSV14525593.xml','r') as file:
    k = file.read()
xml = xmltodict.parse(k)['Файл']
xml = ast.literal_eval(json.dumps(xml))
# for i in xml['ВЫПБНДОПОЛ']['Операции']:
#     print(i['@ИдБлок'])
#     print(i['РеквБанка']['@НомКорСч'])

for i in xml['ВЫПБНДОПОЛ']['Операции']:
    data = {
    'НомСч' : getdata(i)[0],
    'ДатаОпер' : getdata(i)[1],
    'НазнПл' : getdata(i)[2],
    'НаимПП' : getdata(i)[3],
    'Инн': getdata(i)[4],
        
}
    print(data)



