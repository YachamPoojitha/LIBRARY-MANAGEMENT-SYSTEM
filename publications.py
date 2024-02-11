#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# publications.py

import sqlite3

class Publication:
    def __init__(self, publication_id, name):
        self.publication_id = publication_id
        self.name = name

class PublicationManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_publication_table(self):
        # Create the Publication table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS publications (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL)''')

    def add_publication(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO publications (name) VALUES (?)", (name,))
            conn.commit()

    def get_all_publications(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM publications")
            rows = cursor.fetchall()
            publications = []
            for row in rows:
                publication = Publication(row[0], row[1])
                publications.append(publication)
            return publications

