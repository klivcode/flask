import sqlite3

db=sqlite3.connect("site.db")

cursor=db.cursor()

cursor.execute(
    '''
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    '''
)


db.commit()
db.close()