#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import sqlite3

class BookLanguage:
    def __init__(self, language_id, name):
        self.language_id = language_id
        self.name = name

class BookLanguageManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_language_table(self):
        # Create the BookLanguage table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS book_languages (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL)''')

    def add_language(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO book_languages (name) VALUES (?)", (name,))
            conn.commit()

    def get_all_languages(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_languages")
            rows = cursor.fetchall()
            languages = []
            for row in rows:
                language = BookLanguage(row[0], row[1])
                languages.append(language)
            return languages

