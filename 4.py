from distutils.sysconfig import get_config_h_filename
import requests
from bs4 import BeautifulSoup as BS
import csv

class Parser:
    HOST = "https://minfin.com.ua"
    URL = "https://www.youtube.com/watch?v=gy_YlibMW6Q"
    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20220217.00.00',
        
    }

    def __init__(self) -> None:
        self.url = Parser.URL
    
    def get_page(self, params=''):
        self.r = requests.get(self.url, headers=Parser.HEADERS, params=params)
        return self.r
    
    def get_content(self):
        soup = BS(self.get_page().text, 'html.parser')
        with open('d:/GIT/NCFUcarddecoding/file.html', 'w', encoding='utf-8') as r:
            r.write(str(soup))
        items = soup.find_all('label')
        cards = []
        print(items)
        for item in items:
            print(item)
            cards.append(
                {
                  'title': item.find('a','cpshbz-0 eRamNS').text,
                #   'link': f"{Parser.HOST}{item.find('a','cpshbz-0 eRamNS').get('href')}",
                #   'bankname':  item.find('a','be80pr-35 UOQtz').get('alt'),
                #   'cardimg': item.find('img','be80pr-10 jIGseK').get('src'),
                }
            )
        return cards

        
        
        
        
        
        
def main():
    p = Parser()
    p.get_content()
    
if __name__ == '__main__':
    main()
        


