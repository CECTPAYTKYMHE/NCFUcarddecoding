import requests
from bs4 import BeautifulSoup as BS
import csv
import time
class Parser:
    # HOST = "https://minfin.com.ua"
    # URL = "https://www.youtube.com/watch?v=gy_YlibMW6Q"
    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        # 'x-youtube-client-name': '1',
        # 'x-youtube-client-version': '2.20220217.00.00',
        
    }
    proxylist = {
        # '142.44.136.97:7001',
'141.8.194.115:5006',
'159.65.229.246:20033',
'192.81.225.17:33140',
'45.55.218.100:35384',
# 192.81.225.1:33140
# 20.72.151.144:8118
# 51.222.13.193:10084
# 34.134.60.185:443
# 64.235.204.107:3128
# 98.12.195.129:443
# 192.99.7.189:1534
# 12.151.56.30:80
# 64.124.191.98:32688
# 107.151.182.247:80
# 47.88.10.210:80
# 47.88.85.246:7328
# 103.214.109.69:80
# 34.140.87.13:80
# 178.62.92.133:80
# 88.150.230.197:80
# 51.77.159.133:80
# 23.238.33.186:80
# 51.195.76.214:3128
# 46.30.15.162:8080
# 70.60.96.154:5678
# 51.91.157.66:80
# 104.223.88.232:8118
# 176.31.68.252:20171
# 70.185.95.162:39593
    }
    def __init__(self,url) -> None:
        self.url = url
    
    def get_page(self, params=''):
        # for proxy in Parser.proxylist:
        #     print(proxy)
        self.r = requests.get(self.url, headers=Parser.HEADERS, params=params)
                            #   es={"http://": proxy, "https://": proxy})
        # src = self.r.text
        # with open('c:/git/NCFUcarddecoding/index.html','w',encoding='utf-8') as file:
        #     file.write(src)
        return self.r
    
    def get_content(self):
        # with open('c:/git/NCFUcarddecoding/index.html','r',encoding='utf-8') as file:
        #     src = file.read()
        
        soup = BS(self.get_page().text, 'html.parser')
        # with open('C:/GIT/NCFUcarddecoding/file.html', 'w', encoding='utf-8') as r:
        #     r.write(str(soup))
        items = soup.find_all('div', 'iva-item-content-rejJg')
        cards = []
        # print(items)
        for item in items:
            # print(item)
           
            cards.append(
                {
                  'title': item.find('h3').get_text().replace('\xa0',''),
                  'link': item.find('a').get('href'),
                  'price':  item.find(class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').get_text().replace('\xa0',''),
                  'street': item.find(class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL').find('span').get_text(),
                }
            )
        print(cards)
        return cards

        
        
        
        
        
        
def main():
    # with open('C:/GIT/NCFUcarddecoding/avito.csv','a') as f:
    #         w = csv.DictWriter(f,res[0].keys())
    #         w.writeheader()
    #         f.close()
    for q in range(10):
        p = Parser(f'https://www.avito.ru/stavropol/kvartiry/prodam/1-komnatnye/novostroyka-ASgBAgICA0SSA8YQ5geOUsoIgFk?p={q}')
        # p.get_content()
        res = p.get_content()
        for i in range(len(res)):
            with open('C:/GIT/NCFUcarddecoding/avito.csv','a',encoding='utf-8')as f:
                f.write(f"{res[i]['title']};{res[i]['link']};{res[i]['price']};{res[i]['street']}\n")
                f.close()
            
        # for i in range(len(res)):
        #     with open('C:/GIT/NCFUcarddecoding/avito.csv','a',encoding='utf-8',newline='',) as f:
        #             w = csv.DictWriter(f,res[i].keys())
        #             w.writerow(res[i])
        time.sleep(5)
if __name__ == '__main__':
    main()
        


