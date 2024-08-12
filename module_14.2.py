import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)   
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")


cursor.execute("DELETE FROM Users WHERE id = ?", (6,))  #УДАЛЕНИЕ элемента с id = 6
cursor.execute("SELECT COUNT(*) FROM Users")  #считаю количество user
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")  #считаю сумму балансов всех user
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()