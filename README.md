Project: Library Management System

Author: James Carlson

This project was built as an assignment for Coding Temple.


The library management system is made up of objects from three classes: books, users, and authors.


Each book object holds the following information:
 - Title
 - Author
 - ISBN
 - Genre
 - Publication Date
 - Whether or not the book is available to borrow
 - Who the book is borrowed by, if anyone


Each user object holds the following information:
 - Name
 - Library ID - This ID number is set incrementally.
 - Borrowed Books - A list of book titles currently on loan to this user


 Each author object holds the following information:
 - Name
 - Biography
 - Books in Library - A list of book titles by this author within the library system



Using the command-line interface, the user will be prompted with the following options:

1. Book Operations - 
    Handling books within the library system. These options include:
    1. Add a new book
    2. Add a new book by genre - calls on subclasses with genre already set to a featured genre
    3. Borrow a book
    4. Return a checked out book
    5. Search for a book
    6. Display all books

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

4. Export Library to File - 
    Export all library data in the application to a text file.

5. Import Library from File - 
    Import data from a saved file, and use it to populate the library within the application.
    An example file ("library_data/library_export.txt") has been provided in this project folder and can be loaded into the application using this function.

Thank you for reviewing my code and for using the Library Management System!