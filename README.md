Project: Library Management System

Author: James Carlson

This project was built as an assignment for Coding Temple.


The library management system is based on the previous project, but now the database is handled with calls to SQL tables:


Books table:
 - book_id (Primary Key)
 - Title
 - author_id (Foreign Key for Author table)
 - ISBN
 - Genre
 - Publication Date
 - Whether or not the book is available to borrow
 - borrower_id (Foreign Key for Library_Users table) - Who the book is borrowed by, if anyone


Library_Users table:
 - user_id (Primary Key)
 - Name
 - Borrowed Books - Text comprised of book titles currently on loan to this user


 Authors table:
 - author_id (Primary Key)
 - Name
 - Biography
 - Books in Library - Text comprised of book titles by this author within the library system



Using the command-line interface, the user will be prompted with the following options:

1. Book Operations - 
    Handling books within the library system. These options include:
    1. Add a new book
    2. Borrow a book
    3. Return a checked out book
    4. Search for a book
    5. Display all books

2. User Operations - 
    Handles users within the library system. Options include:
    1. Add a new user
    2. View user details
    3. Display all users

3. Author Operations - 
    Handles authors within the library system. Options include:
    1. Add a new author
    2. View author details
    3. Display all authors



Thank you for reviewing my code and for using the Library Management System!