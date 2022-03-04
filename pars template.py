import re
from webbrowser import get
import requests
from bs4 import BeautifulSoup as BS
import csv
import time
import json
from urllib.parse import urlparse
import ast
wildberries = 'www.wildberries.ru'
ozon = 'www.ozon.ru'

HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
}
def get_page_url(url,params=''):
        # for proxy in Parser.proxylist:
        #     print(proxy)
        r = requests.get(url, headers=HEADERS, params=params, timeout=60)
                            #   es={"http://": proxy, "https://": proxy})
        src = r.text
        with open('D:/git/163/index.html','w',encoding='utf-8') as file:
            file.write(src)
        return r
def get_content():
        with open('d:/git/163/index.html','r',encoding='utf-8') as file:
            src = file.read()
        with open('d:/git/163/index.txt','w',encoding='utf-8') as file:
            file.write(src)
        soup = BS(src, 'html.parser')
        # soup = BS(get_page_url(url).text, 'html.parser')
        cards = []
        data = soup.find('script') 
        data = str(data)
        

# get_page_url('https://buff.163.com/')
get_content()