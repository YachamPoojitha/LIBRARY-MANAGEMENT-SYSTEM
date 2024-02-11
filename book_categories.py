#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# book_categories.py

import sqlite3

class BookCategory:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

class BookCategoryManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_category_table(self):
        # Create the BookCategory table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS book_categories (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL)''')

    def add_category(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO book_categories (name) VALUES (?)", (name,))
            conn.commit()

    def get_all_categories(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_categories")
            rows = cursor.fetchall()
            categories = []
            for row in rows:
                category = BookCategory(row[0], row[1])
                categories.append(category)
            return categories

