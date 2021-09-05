"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete entry
Close
"""

from tkinter import *
import sqlite3

import backend


def view_command():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)

def search_command(title, author, year, isbn):
    listbox.delete(0, END)


window = Tk()
window.title("Book store")
title_label = Label(window, text="Title")
author_label = Label(window, text="Author")
year_label = Label(window, text="Year")
isbn_label = Label(window, text="ISBN")

title_text, author_text, year_text, isbn_text = StringVar(), StringVar(), StringVar(), StringVar()
title_entry = Entry(window, textvariable=title_text)
author_entry = Entry(window, textvariable=author_text)
year_entry = Entry(window, textvariable=year_text)
isbn_entry = Entry(window, textvariable=isbn_text)

title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)
author_label.grid(row=0, column=2)
author_entry.grid(row=0, column=3)
year_label.grid(row=1, column=0)
year_entry.grid(row=1, column=1)
isbn_label.grid(row=1, column=2)
isbn_entry.grid(row=1, column=3)

listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scroll.set)
scroll.configure(command=listbox.yview)

view_btn = Button(window, text="View all", width=14, command=view_command)
search_btn = Button(window, text="Search entry", width=14, command=search_command)
add_btn = Button(window, text="Add entry", width=14)
update_btn = Button(window, text="Update", width=14)
delete_btn = Button(window, text="Delete", width=14)
close_btn = Button(window, text="Close", width=14)

view_btn.grid(row=2, column=3)
search_btn.grid(row=3, column=3)
add_btn.grid(row=4, column=3)
update_btn.grid(row=5, column=3)
delete_btn.grid(row=6, column=3)
close_btn.grid(row=7, column=3)

window.mainloop()
