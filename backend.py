import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

# def update(id, title, author, year, isbn):
#     conn = sqlite3.connect("books.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM book WHERE id=?", (id,))
#     row = cur.fetchall()[0]

#     args = (title, author, year, isbn)
#     new_row = []
#     for arg_enum in enumerate(args, 1):
#         new_row.append(row[arg_enum[0]] if arg_enum[1] == "" else arg_enum[1])
#     delete(row[0])
#     insert(*new_row)
#     conn.commit()
#     conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    # args = (title, author, year, isbn)
    # new_row = []
    # # for arg_enum in enumerate(args, 1):
    # #     new_row.append(row[arg_enum[0]] if arg_enum[1] == "" else arg_enum[1])
    # # delete(row[0])
    # # insert(*new_row)

    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
# insert("The Earth", "Sam Travalta", 2002, 2345345633)

update(2, "Harry Potter and the goblet of fire", "J.K. Rowling", "", "")
print(view())