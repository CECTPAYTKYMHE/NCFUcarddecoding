import sqlite3
import time
from wildberriespars import get_content
# all = []
# connect = sqlite3.connect('C:/GIT/bot/users.db')
# cursor = connect.cursor()
# cursor.execute(f"SELECT url,id FROM urls WHERE link_id = 687724238")
# count = cursor.fetchall()
# for i in count:
#     all.append(i[1])
# print(all)
# from urllib.parse import urlparse
# k = urlparse('https://www.wildberries.ru/catalog/11229881/detail.aspx?targetUrl=GP')
# print(k.netloc)
# price = '\n                    1\xa0466\xa0₽\n                '
# print(price.replace('\xa0','').replace('₽','').split())
connect = sqlite3.connect('C:/GIT/bot/users.db')
cursor = connect.cursor()
cursor.execute("SELECT link_id,url,price,id FROM urls")
data = cursor.fetchall()
for i in data:
    title, price = get_content(i[1])
    print(title,price)
    if price < i[2]:
        cursor.execute(f"UPDATE urls SET price = (?) WHERE link_id = {i[0]} AND id = {i[3]} ",(price,))
        print(i[0],f'Товар подешевел на {int(i[2]) - int(price)}')
        connect.commit()
connect.close()

