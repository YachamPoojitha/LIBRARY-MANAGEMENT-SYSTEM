#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# main.py

from admin import Admin
from authors import AuthorManager
from book_categories import BookCategoryManager
from book_languages import BookLanguageManager
from books import BookManager
from publications import PublicationManager
from students import StudentManager
from issue_books import IssueBookManager
from reports import ReportGenerator

DB_NAME = "library.db"

def create_tables():
    author_manager = AuthorManager(DB_NAME)
    author_manager.create_author_table()

    category_manager = BookCategoryManager(DB_NAME)
    category_manager.create_category_table()

    language_manager = BookLanguageManager(DB_NAME)
    language_manager.create_language_table()

    book_manager = BookManager(DB_NAME)
    book_manager.create_book_table()

    publication_manager = PublicationManager(DB_NAME)
    publication_manager.create_publication_table()

    student_manager = StudentManager(DB_NAME)
    student_manager.create_student_table()

    issue_book_manager = IssueBookManager(DB_NAME)
    issue_book_manager.create_issue_book_table()

def main():
    admin_user = Admin(username="admin", password="password")

    print("Welcome to the Library Management System")

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if admin_user.login(username, password):
            print("Login successful.")
            break
        else:
            print("Invalid credentials. Try again.")

    create_tables()

    while True:
        print("Dashboard for Admin User")
        print("1. Add new author")
        print("2. Add new book category")
        print("3. Add new book language")
        print("4. Add new book")
        print("5. Add new publication")
        print("6. Add new student")
        print("7. Issue a book to a student")
        print("8. Generate reports")
        print("9. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the author's name: ")
            email = input("Enter the author's email: ")
            author_manager = AuthorManager(DB_NAME)
            author_manager.add_author(name, email)
            print("Author added successfully!")

        elif choice == "2":
            name = input("Enter the book category name: ")
            category_manager = BookCategoryManager(DB_NAME)
            category_manager.add_category(name)
            print("Book category added successfully!")

        elif choice == "3":
            name = input("Enter the book language name: ")
            language_manager = BookLanguageManager(DB_NAME)
            language_manager.add_language(name)
            print("Book language added successfully!")

        elif choice == "4":
            title = input("Enter the book title: ")
            author_id = int(input("Enter the author's ID: "))
            category_id = int(input("Enter the category's ID: "))
            language_id = int(input("Enter the language's ID: "))
            publication_id = int(input("Enter the publication's ID: "))
            book_manager = BookManager(DB_NAME)
            book_manager.add_book(title, author_id, category_id, language_id, publication_id)
            print("Book added successfully!")

        elif choice == "5":
            name = input("Enter the publication name: ")
            publication_manager = PublicationManager(DB_NAME)
            publication_manager.add_publication(name)
            print("Publication added successfully!")

        elif choice == "6":
            name = input("Enter the student's name: ")
            email = input("Enter the student's email: ")
            student_manager = StudentManager(DB_NAME)
            student_manager.add_student(name, email)
            print("Student added successfully!")

        elif choice == "7":
            book_id = int(input("Enter the book ID: "))
            student_id = int(input("Enter the student ID: "))
            issue_date = input("Enter the issue date (YYYY-MM-DD): ")
            return_date = input("Enter the return date (YYYY-MM-DD): ")
            issue_book_manager = IssueBookManager(DB_NAME)
            issue_book_manager.add_issue_book(book_id, student_id, issue_date, return_date)
            print("Book issued successfully!")

        elif choice == "8":
            report_gen = ReportGenerator(DB_NAME)
            print(report_gen.generate_all_authors_report())
            print(report_gen.generate_all_book_categories_report())
            print(report_gen.generate_all_book_languages_report())
            print(report_gen.generate_all_books_report())
            print(report_gen.generate_all_publications_report())
            print(report_gen.generate_all_students_report())
            print(report_gen.generate_all_issue_books_report())

        elif choice == "9":
            print("Logged out. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

