import re
import requests
from bs4 import BeautifulSoup as BS
import csv
import time
import json
HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
}
def get_page_url(url,params=''):
        # for proxy in Parser.proxylist:
        #     print(proxy)
        r = requests.get(url, headers=HEADERS, params=params)
                            #   es={"http://": proxy, "https://": proxy})
        # src = r.text
        # with open('c:/git/files/wild/ozon.html','w',encoding='utf-8') as file:
        #     file.write(src)
        return r
def get_content(url):
        with open('c:/git/files/wild/ozon.html','r',encoding='utf-8') as file:
                src = file.read()
        # soup = BS(src, 'html.parser')
        soup = BS(get_page_url(url).text, 'html.parser')
        cards = []
        try:
                cards.append({'title': soup.find('h1',class_='j6r').get_text()})
                cards.append({'price':  soup.find('span',class_='jq4 j4q').get_text()})
                return (cards[0]['title'], cards[1]['price'].replace('\u2009','').replace('₽\xa0','').split()[0])
        except:
                title = None
                price = None
                return (title,price)
        
