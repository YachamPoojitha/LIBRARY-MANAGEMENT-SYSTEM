#!/usr/bin/env python
# coding: utf-8

# In[3]:


# reports.py
import sqlite3

class ReportGenerator:
    def __init__(self, db_name):
        self.db_name = db_name

    def generate_all_authors_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            rows = cursor.fetchall()
            report = "All Authors:\n"
            for row in rows:
                report += f"{row[1]} - {row[2]}\n"
            return report

    def generate_all_book_categories_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_categories")
            rows = cursor.fetchall()
            report = "All Book Categories:\n"
            for row in rows:
                report += f"{row[1]}\n"
            return report

    def generate_all_book_languages_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_languages")
            rows = cursor.fetchall()
            report = "All Book Languages:\n"
            for row in rows:
                report += f"{row[1]}\n"
            return report

    def generate_all_books_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            report = "All Books:\n"
            for row in rows:
                report += f"{row[1]}\n"
            return report

    def generate_all_publications_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM publications")
            rows = cursor.fetchall()
            report = "All Publications:\n"
            for row in rows:
                report += f"{row[1]}\n"
            return report

    def generate_all_students_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            report = "All Students:\n"
            for row in rows:
                report += f"{row[1]} - {row[2]}\n"
            return report

    def generate_all_issue_books_report(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT ib.id, b.title, s.name, ib.issue_date, ib.return_date
                              FROM issue_books ib
                              JOIN books b ON ib.book_id = b.id
                              JOIN students s ON ib.student_id = s.id''')
            rows = cursor.fetchall()
            report = "All Issue Books:\n"
            for row in rows:
                report += f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}\n"
            return report


# In[ ]:




