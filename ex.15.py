import sqlite3 as sq
with sq.connect("fox.db") as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    old INTEGER PRIMARY KEY,
    score INTEGER 
    )''')
