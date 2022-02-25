import telebot
from telebot import types
import sqlite3
import time


token=''
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def registering(message):
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        datetime_register TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS urls(
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
        bot.send_message(message.chat.id,'Привет, пользователь ' + message.from_user.username + ' зарегистрирован')
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы')
        bot.send_sticker(message.chat.id,sticker='f55bf319-3d94-4344-aa93-b2030d97db03')
    connect.close()
    
def save_url(message):
    user_id = message.chat.id
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO 'urls' ('link_id','url') VALUES(?,?)",(user_id,message.text))
    connect.commit()
    connect.close()
    
@bot.message_handler(commands=['url'])
def get_url(message):
    sent = bot.send_message(message.chat.id, 'Введите url')
    bot.register_next_step_handler(sent, save_url)

@bot.message_handler(commands=['geturl'])
def get_all_my_url(message):
    user_id = message.chat.id 
    connect = sqlite3.connect('D:/GIT/bot/users.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT url FROM urls WHERE link_id = {user_id}")
    data = cursor.fetchall()
    for i in data:
        bot.send_message(message.chat.id,i)
        
    

@bot.message_handler(commands=['delete'])
def delete(message):
    pass
    


    
# Запускаем бота
def main():
    bot.polling(none_stop=True, interval=0)
if __name__ == '__main__':
    main()


