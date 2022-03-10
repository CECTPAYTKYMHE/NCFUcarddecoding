from tabnanny import check
import telebot
from telebot import types
import sqlite3
import time
from urllib.parse import urlparse
from wildberriespars import get_content
token='5269012443:AAFbM7AKJLkN7senATwZvAcYkBQypud2dVA'
bot=telebot.TeleBot(token)

def check_price():
    while True:
        connect = sqlite3.connect('C:/GIT/bot/users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT link_id,url,price,id FROM urls")
        data = cursor.fetchall()
        for i in data:
            title, price = get_content(i[1])
            print(title,price)
            if price < i[2]:
                cursor.execute(f"UPDATE urls SET price = (?) WHERE link_id = {i[0]} AND id = {i[3]} ",(price,))
                connect.commit()
                bot.send_message(i[0],f'{i[1]}\n{"~"*20}\nТовар подешевел на {int(i[2]) - int(price)}')
        connect.close()
        time.sleep(15)
        print('yes')
if __name__ == '__main__':
    check_price()