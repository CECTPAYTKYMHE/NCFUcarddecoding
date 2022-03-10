import re
import requests
from bs4 import BeautifulSoup as BS
import csv
import time
import json
import ast
from urllib.parse import urlparse
wildberries = 'www.wildberries.ru'
ozon = 'www.ozon.ru'

HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
}
def get_page_url(url,params=''):
        # for proxy in Parser.proxylist:
        #     print(proxy)
        r = requests.get(url, headers=HEADERS, params=params)
                            #   es={"http://": proxy, "https://": proxy})
        src = r.text
        with open('c:/git/files/wild/ozon3.html','w',encoding='utf-8') as file:
            file.write(src)
        return r
def get_content(url):
        with open('c:/git/files/wild/ozon2.html','r',encoding='utf-8') as file:
            src = file.read()
        # soup = BS(src, 'html.parser')
        soup = BS(get_page_url(url).text, 'html.parser')
        cards = []
        with open('C:/GIT/files/wild/ozon3.txt', 'w',encoding='utf-8') as file:
                file.write(str(soup))
        # print(soup)
        data = soup.find('script', type='application/ld+json')
        data = str(data)
        data = data.replace('<script data-n-head="true" type="application/ld+json">','').replace('/script','').replace('<>','')
        data = ast.literal_eval(data)
        print(data['offers']['price'])
        print(data['name'])
        cards.append(data['name'])
        cards.append(data['offers']['price'])
        print(cards[0])
        print(cards[1])
        # print(json.loads(data))
        # try:
        #     if urlparse(url).netloc == wildberries:
        #         cards.append({'title': soup.find('meta',property='og:title').get('content')})
        #         cards.append({'price':  soup.find(class_='price-block__final-price').get_text()})
        #         return (cards[0]['title'], cards[1]['price'].replace('\xa0','').replace('₽','').split()[0])
        #     elif urlparse(url).netloc == ozon:
        # cards.append({'title': soup.find('h1',class_='j6r').get_text()})
        # cards.append({'price':  soup.find('span',class_='jq4 j4q').get_text()})
        # return (cards[0]['title'], cards[1]['price'].replace('\u2009','').replace('₽\xa0','').split()[0])
        # except:
        #     title = None
        #     price = None
        #     return (title,price)
# get_page_url('https://www.ozon.ru/product/suhoy-korm-purina-one-dlya-sterilizovannyh-koshek-i-kotov-s-govyadinoy-i-pshenitsey-3-kg-150030882/?_bctx=CAYQjtkQ&asb=BELV%252FgjQlIBG1djPc%252F01I6cXOzMzc6Sl9shWR3THCPU%253D&asb2=r7zRy_x6TF5HzOX4mnSTvAcPQn6r-YU4r-B0t-F87ioEAtr8lKwK0FTZIPbXoENXefmwz9SW9OHAcqS1PTEu2Q&sh=H6k06AAAAA')
print(get_content('https://www.ozon.ru/product/ultrazvukovaya-chistka-wellskins-ultrasonic-skin-scrubber-282671007/?sh=SjSipQAAAA'))