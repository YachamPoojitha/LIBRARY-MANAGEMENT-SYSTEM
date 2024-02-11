#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# authors.py

import sqlite3

class Author:
    def __init__(self, author_id, name, email):
        self.author_id = author_id
        self.name = name
        self.email = email

class AuthorManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_author_table(self):
        # Create the Author table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL,
                              email TEXT NOT NULL)''')

    def add_author(self, name, email):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name, email) VALUES (?, ?)", (name, email))
            conn.commit()

    def get_all_authors(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            rows = cursor.fetchall()
            authors = []
            for row in rows:
                author = Author(row[0], row[1], row[2])
                authors.append(author)
            return authors

