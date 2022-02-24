import requests
from bs4 import BeautifulSoup as BS
import csv
import time
class Parser:
    
    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
       
        
    }
    proxylist = {
        '142.44.136.97:7001',
'141.8.194.115:5006',
'159.65.229.246:20033',
'192.81.225.17:33140',
'45.55.218.100:35384',
'192.81.225.1:33140',
'20.72.151.144:8118',
'51.222.13.193:10084',
    }
    def __init__(self,url) -> None:
        self.url = url
    
    def get_page(self, params=''):
        # for proxy in Parser.proxylist:
        self.r = requests.get(self.url, headers=Parser.HEADERS, params=params)
                            #   proxies={"http://": proxy, "https://": proxy})
        # src = self.r.text
        # with open('c:/git/files/index.html','w',encoding='utf-8') as file:
        #     file.write(src)
        return self.r
    
    def get_content(self):
        # with open('c:/git/files/index.html','r',encoding='utf-8') as file:
        #     src = file.read()
        
        soup = BS(self.get_page().text, 'html.parser')
        items = soup.find_all('div', 'iva-item-content-rejJg')
        cards = []
        # print(items)
        for item in items:
            # print(item)
            cards.append(
                {
                  'title': item.find('h3').get_text().replace('\xa0',''),
                  'link': 'https://www.avito.ru' + item.find('a').get('href'),
                  'price':  item.find(class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').get_text().replace('\xa0',''),
                  'street': item.find(class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL').find('span').get_text(),
                }
            )
        # print(cards)
        return cards

       
def main():
    for q in range(3):
        p = Parser(f'https://www.avito.ru/stavropol/kommercheskaya_nedvizhimost/sdam/drugoe-ASgBAQICAUSwCNRWAUCeww0Uhtk5?cd=1&district=289-290-291&f=ASgBAQECAkSwCNRW9BKk2gEBQJ7DDRSG2TkBRbYTFXsiZnJvbSI6bnVsbCwidG8iOjgwfQ&p={q}')
        # p.get_content()
        res = p.get_content()
        for i in range(len(res)):
            with open('C:/GIT/files/avitocomm.csv','a',encoding='utf-8')as f:
                f.write(f"{res[i]['title']};{res[i]['link']};{res[i]['price']};{res[i]['street']}\n")
                f.close()
        time.sleep(5)
if __name__ == '__main__':
    main()
        


