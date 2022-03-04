import telebot
from telebot import types
import sqlite3
import time
from telebot import apihelper

token='5174028836:AAFA9fKL8tLd5hs8FxEEvdhMD4k_v5I7ebM'
bot=telebot.TeleBot(token)

apihelper.proxy = {'https':'socks5://telegram:telegram@109.238.222.5:42401'}

@bot.message_handler(commands=['start'])
def registering(message):
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        datetime_register TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS urls(
        id INTEGER PRIMARY KEY,
        link_id INTEGER,
        url TEXT,
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
    buttons(message)
    
def buttons(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Добавить URL',callback_data='seturl')
    item2 = types.InlineKeyboardButton('Показать все мои URL',callback_data='getallurl')
    item3 = types.InlineKeyboardButton('Удалить все мои URL',callback_data='deleteallurl')
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id, 'Нажимай', reply_markup=markup)
    
    
def save_url(message):
    user_id = message.chat.id
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute('SELECT COUNT(*) from urls')
    count = cursor.fetchone()[0]
    count += 1
    cursor.execute("INSERT INTO 'urls' (id,'link_id','url') VALUES(?,?,?)",(count,user_id,message.text))
    connect.commit()
    connect.close()
    buttons(message)
    

def set_url(message):
        sent = bot.send_message(message.chat.id, 'Введите url')
        bot.register_next_step_handler(sent, save_url)
        


def get_all_my_url(message):
    user_id = message.chat.id 
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT url FROM urls WHERE link_id = {user_id}")
    data = cursor.fetchall()
    for i in data:
        bot.send_message(message.chat.id,i)
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

def del_url(message):
    sent = bot.send_message(message.chat.id, 'Введите номер удаляемого url')
    bot.register_next_step_handler(sent, delete_url)
    
@bot.message_handler(commands=['delete'])
def delete_url(message):
    
    user_id = message.chat.id 
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute(f"DELETE FROM urls WHERE link_id = {user_id}")
    connect.commit()
    connect.close()
    buttons(message)             

@bot.message_handler(commands=['delete'])
def delete_all_url(message):
    user_id = message.chat.id 
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute(f"DELETE FROM urls WHERE link_id = {user_id}")
    connect.commit()
    connect.close()
    buttons(message)
    


    
# Запускаем бота
def main():
    bot.polling(none_stop=True, interval=0)
if __name__ == '__main__':
    main()


