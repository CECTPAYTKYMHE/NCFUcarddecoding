import telebot
from telebot import types
import sqlite3
import time
from urllib.parse import urlparse
from wildbozon import get_content
import threading
import botsettings

sites = ['www.ozon.ru','www.wildberries.ru']
# ozon = 'www.ozon,ru'
# wild = 'www.wildberries.ru'

token = botsettings.token
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def registering(message):
    connect = sqlite3.connect(botsettings.db)
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        datetime_register TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS urls(
        id INTEGER,
        link_id INTEGER,
        url TEXT,
        price,
        title,
        FOREIGN KEY(link_id) REFERENCES users(id)
        )""")
    connect.commit()
    people = message.chat.id
    cursor.execute(f"SELECT id FROM users WHERE id = {people}")
    data = cursor.fetchone()
    if data is None:
        dt = time.strftime('%Y/%m/%d %H:%M:%S')
        user_id = message.chat.id
        cursor.execute("INSERT INTO 'users' ('id', 'datetime_register') VALUES(?,?)",(user_id,dt))
        connect.commit()
        bot.send_message(message.chat.id,'Привет, вы зарегистрированы')
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы')
    connect.close()
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Меню')
    buttons(message)

@bot.message_handler(commands=['Меню'])
def buttons(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Добавить URL',callback_data='seturl')
    item2 = types.InlineKeyboardButton('Показать все мои URL',callback_data='getallurl')
    item3 = types.InlineKeyboardButton('Удалить все мои URL',callback_data='deleteallurl')
    item4 = types.InlineKeyboardButton('Удалить определенные URL',callback_data='deleteurl')
    markup.add(item1,item2,item3,item4)
    bot.send_message(message.chat.id, 'Выберите пункт меню', reply_markup=markup)

def save_url(message, title = None, price = None):
    id = 1
    all = []
    user_id = message.chat.id
    connect = sqlite3.connect(botsettings.db)
    cursor = connect.cursor()
    cursor.execute(f'SELECT id from urls WHERE link_id = {user_id}')
    count = cursor.fetchall()
    for i in count:
        all.append(i[0])
    while True:
        if id in all:
            id += 1
        else:
            break
    if urlparse(message.text).netloc not in sites:
        bot.send_message(message.chat.id, 'Это ссылка не OZON или Wildberries')
    else:
        title, price = get_content(message.text)
        cursor.execute("INSERT INTO 'urls' (id,'link_id','url',title,price) VALUES(?,?,?,?,?)",(id,user_id,message.text,title,price))
        connect.commit()
        connect.close()
    buttons(message)
    
def set_url(message):
        sent = bot.send_message(message.chat.id, 'Введите url')
        bot.register_next_step_handler(sent, save_url)

def get_all_my_url(message):
    user_id = message.chat.id 
    connect = sqlite3.connect(botsettings.db)
    cursor = connect.cursor()
    cursor.execute(f"SELECT url,id FROM urls WHERE link_id = {user_id} ORDER BY id")
    data = cursor.fetchall()
    if len(data) == 0:
        bot.send_message(message.chat.id, 'У вас нету сохраненных ссылок')
    for i in data:
        bot.send_message(message.chat.id,f'{i[0]} \nНомер ссылки = {i[1]}')   
    buttons(message)
        
@bot.callback_query_handler(func=lambda call :True)  
def callback(call):
    if call.message:
        if call.data == 'seturl':
            set_url(call.message)
        elif call.data == 'getallurl':
            get_all_my_url(call.message)
        elif call.data == 'deleteallurl':
            delete_all_url(call.message)
        elif call.data == 'deleteurl':
            del_url(call.message)

def del_url(message):
    sent = bot.send_message(message.chat.id, 'Введите номер удаляемых url через пробел')
    bot.register_next_step_handler(sent, delete_url)
    
    
# @bot.message_handler(commands=['delete'])
def delete_url(message):
    numbers = message.text.split()
    user_id = message.chat.id 
    connect = sqlite3.connect(botsettings.db)
    cursor = connect.cursor()
    for i in numbers:
        i = int(i)
        cursor.execute(f"DELETE FROM urls WHERE id = {i}")
    connect.commit()
    connect.close()
    buttons(message)             

# @bot.message_handler(commands=['deleteall'])
def delete_all_url(message):
    user_id = message.chat.id 
    connect = sqlite3.connect(botsettings.db)
    cursor = connect.cursor()
    cursor.execute(f"DELETE FROM urls WHERE link_id = {user_id}")
    connect.commit()
    connect.close()
    buttons(message)
    
def check_price():
    while True:
        connect = sqlite3.connect(botsettings.db)
        cursor = connect.cursor()
        cursor.execute("SELECT link_id,url,price,id FROM urls")
        data = cursor.fetchall()
        for i in data:
            title, price = get_content(i[1])
            if int(price) < int(i[2]):
                print('price<i2')
                cursor.execute(f"UPDATE urls SET price = (?) WHERE link_id = {i[0]} AND id = {i[3]} ",(price,))
                connect.commit()
                print(f'{i[1]}\n{"~"*20}\nТовар подешевел на {int(i[2]) - int(price)}')
                bot.send_message(i[0],f'{i[1]}\n{"~"*20}\nТовар подешевел на {int(i[2]) - int(price)}')
        connect.close()
        time.sleep(1800)
        

    
# Запускаем бота
def main():
    bot.polling(none_stop=True, interval=0)
    
if __name__ == '__main__':
    try:
        thread1 = threading.Thread(target=check_price)
        thread1.start()
        thread2 = threading.Thread(target=main)
        thread2.start()
    except KeyboardInterrupt:
        print ('Interrupted')
        exit(0)

  


