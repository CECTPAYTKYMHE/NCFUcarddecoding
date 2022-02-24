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
        src = r.text
        with open('c:/git/files/oxl/index.html','w',encoding='utf-8') as file:
            file.write(src)
        return
    
def get_phone(id,url):
    headers = {
        'Host': 'www.olx.ua',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
        'X-Platform-Type': 'mobile-html5',
        'Version': 'v1.19',
        'Accept-Language': 'ru',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'Bearer 03bd5aac1dab0ef5f1703bac90cd12b7d4074ccf',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'X-Client': 'DESKTOP',
        'X-Device-Id': 'ef8f4a03-aa84-436f-887f-78d70f3682ee',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.olx.ua/d/obyavlenie/zdam-v-orendu-primschennya-po-vul-o-telgi-61-IDNPUhF.html',
        'Accept-Encoding': 'gzip, deflate',
    }

    response = requests.get(f'https://www.olx.ua/api/v1/offers/{id}/limited-phones/', headers=headers,  verify=False)
    phone = response.content
    phone = json.loads(phone)
    return phone['data']['phones'][0]

def get_content():
        with open('c:/git/files/oxl/index.html','r',encoding='utf-8') as file:
            src = file.read()
        soup = BS(src, 'html.parser')
        # soup = BS(get_page_url().text, 'html.parser')
        items = soup.find_all('div', 'offer-wrapper')
        cards = []
        # print(items[:1])
        for item in items[:1]:
            # print(item)
           
            cards.append(
                {
                   'id': item.find('table').get('data-id'),
                  'title': item.find(class_='lheight22 margintop5').find('strong').get_text(),
                  'link':  item.find('a').get('href').split('#')[0],
                  'price':  item.find(class_='price').find('strong').get_text(),
                  'city': item.find(class_='bottom-cell').find('span').get_text(),
                  'phone': get_phone(item.find('table').get('data-id'),item.find('a').get('href').split('#')[0])
                }
            )
        print(cards)
        # for i in range(len(cards)):
        #     with open('c:/git/files/oxl/oxl.csv','a',encoding='cp1251') as f:
        #         f.write(f"{cards[i]['title']};{cards[i]['link']};{cards[i]['price']};{cards[i]['city']}\n")
        #         f.close()
                
        
# get_phone()
get_content()  
# get_page_url('https://www.olx.ua/nedvizhimost/')