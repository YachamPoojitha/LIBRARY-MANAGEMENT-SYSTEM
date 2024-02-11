#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# students.py

import sqlite3

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

class StudentManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_student_table(self):
        # Create the Student table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL,
                              email TEXT NOT NULL)''')

    def add_student(self, name, email):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
            conn.commit()

    def get_all_students(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            students = []
            for row in rows:
                student = Student(row[0], row[1], row[2])
                students.append(student)
            return students

