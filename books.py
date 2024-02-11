#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# books.py

import sqlite3

class Book:
    def __init__(self, book_id, title, author_id, category_id, language_id, publication_id):
        self.book_id = book_id
        self.title = title
        self.author_id = author_id
        self.category_id = category_id
        self.language_id = language_id
        self.publication_id = publication_id

class BookManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_book_table(self):
        # Create the Book table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              title TEXT NOT NULL,
                              author_id INTEGER NOT NULL,
                              category_id INTEGER NOT NULL,
                              language_id INTEGER NOT NULL,
                              publication_id INTEGER NOT NULL,
                              FOREIGN KEY (author_id) REFERENCES authors(id),
                              FOREIGN KEY (category_id) REFERENCES book_categories(id),
                              FOREIGN KEY (language_id) REFERENCES book_languages(id),
                              FOREIGN KEY (publication_id) REFERENCES publications(id))''')

    def add_book(self, title, author_id, category_id, language_id, publication_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO books (title, author_id, category_id, language_id, publication_id)
                              VALUES (?, ?, ?, ?, ?)''', (title, author_id, category_id, language_id, publication_id))
            conn.commit()

    def get_all_books(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT b.id, b.title, a.name, c.name, l.name, p.name
                              FROM books b
                              JOIN authors a ON b.author_id = a.id
                              JOIN book_categories c ON b.category_id = c.id
                              JOIN book_languages l ON b.language_id = l.id
                              JOIN publications p ON b.publication_id = p.id''')
            rows = cursor.fetchall()
            books = []
            for row in rows:
                book = Book(row[0], row[1], row[2], row[3], row[4], row[5])
                books.append(book)
            return books

