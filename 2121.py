import sqlite3
import time
user_id = 12222
dt = time.strftime('%Y/%m/%d %H:%M:%S')
connect = sqlite3.connect('D:/GIT/bot/users.db')
cursor = connect.cursor()
cursor.execute("INSERT INTO 'users' ('id', 'datetime_register') VALUES(?,?)",(user_id,dt))
connect.commit()