import sqlite3


class DB:
    def __init__(self):
        self.db = sqlite3.connect("books.db", check_same_thread=False)
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
        )

    def add_row(self, title, author, rating):
        self.cursor.execute(
            "INSERT INTO books VALUES (NULL, ?, ?, ?)", (title, author, rating)
        )
        self.db.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return [
            {"id": row[0], "title": row[1], "author": row[2], "rating": row[3]}
            for row in rows
        ]


# create db
# db = sqlite3.connect("books.db")
# create cursor
# cursor = db.cursor()

# create table
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )

# add row
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
