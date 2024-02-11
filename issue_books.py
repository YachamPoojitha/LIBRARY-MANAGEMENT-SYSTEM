#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# issue_books.py

import sqlite3

class IssueBook:
    def __init__(self, issue_id, book_id, student_id, issue_date, return_date):
        self.issue_id = issue_id
        self.book_id = book_id
        self.student_id = student_id
        self.issue_date = issue_date
        self.return_date = return_date

class IssueBookManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_issue_book_table(self):
        # Create the IssueBook table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS issue_books (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              book_id INTEGER NOT NULL,
                              student_id INTEGER NOT NULL,
                              issue_date TEXT NOT NULL,
                              return_date TEXT NOT NULL,
                              FOREIGN KEY (book_id) REFERENCES books(id),
                              FOREIGN KEY (student_id) REFERENCES students(id))''')

    def add_issue_book(self, book_id, student_id, issue_date, return_date):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO issue_books (book_id, student_id, issue_date, return_date)
                              VALUES (?, ?, ?, ?)''', (book_id, student_id, issue_date, return_date))
            conn.commit()

    def get_all_issue_books(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT ib.id, b.title, s.name, ib.issue_date, ib.return_date
                              FROM issue_books ib
                              JOIN books b ON ib.book_id = b.id
                              JOIN students s ON ib.student_id = s.id''')
            rows = cursor.fetchall()
            issue_books = []
            for row in rows:
                issue_book = IssueBook(row[0], row[1], row[2], row[3], row[4])
                issue_books.append(issue_book)
            return issue_books

