# import sqlite3
# import time
# all = []
# connect = sqlite3.connect('C:/GIT/bot/users.db')
# cursor = connect.cursor()
# cursor.execute(f"SELECT url,id FROM urls WHERE link_id = 687724238")
# count = cursor.fetchall()
# for i in count:
#     all.append(i[1])
# print(all)
from urllib.parse import urlparse
k = urlparse('https://www.wildberries.ru/catalog/11229881/detail.aspx?targetUrl=GP')
print(k.netloc)