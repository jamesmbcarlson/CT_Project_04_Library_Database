# James Carlson
# Coding Temple - SE FT-144
# Module 5: Mini-Project | Library Management System - Now with SQL!

import re

from library_sql.sql_ops import connect_to_db

from library_classes.book import Book
from library_classes.user import User
from library_classes.author import Author

# format constants
F_UNDERLINE = "\033[4m"
F_RED = "\033[91m"
F_YELLOW = "\033[93m"
F_GREEN = "\033[92m"
F_RESET = "\033[0m"
    
# --- Menu Functions --- #

def menu_main():
    '''
    Display and handle main menu operations.
    '''
    while True:
        # print menu to terminal
        print(f"\n{F_GREEN}{F_UNDERLINE}Main Menu:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Book Operations")
        print(f"{F_YELLOW}2{F_RESET}. User Operations")
        print(f"{F_YELLOW}3{F_RESET}. Author Operations")
        print(f"{F_YELLOW}4{F_RESET}. Quit")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("book"):
            menu_book_operations()
        elif menu_input == "2" or menu_input.startswith("user"):
            menu_user_operations()
        elif menu_input == "3" or menu_input.startswith("author"):
            menu_author_operations()
        elif menu_input == "4" or menu_input.startswith("quit"):
            print("Thank you for using the Library Management System!")
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

def menu_book_operations():
    '''
    Display and handle book menu operations.
    '''
    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}Book Operations:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Add a new book")
        print(f"{F_YELLOW}2{F_RESET}. Borrow a book")
        print(f"{F_YELLOW}3{F_RESET}. Return a book")
        print(f"{F_YELLOW}4{F_RESET}. Search for a book")
        print(f"{F_YELLOW}5{F_RESET}. Display all books")
        print(f"{F_YELLOW}6{F_RESET}. Back to main menu")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("add"):
            book_add()
        elif menu_input == "2" or menu_input.startswith("borrow"):
            book_borrow()
        elif menu_input == "3" or menu_input.startswith("return"):
            book_return_submenu()
        elif menu_input == "4" or menu_input.startswith("search"):
            book_search_from_menu()
        elif menu_input == "5" or menu_input.startswith("display"):
            book_display_all()
        elif menu_input == "6" or menu_input.startswith("back"):
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

def menu_user_operations():
    '''
    Display and handle user menu operations.
    '''
    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}User Operations:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Add a new user")
        print(f"{F_YELLOW}2{F_RESET}. View user details")
        print(f"{F_YELLOW}3{F_RESET}. Display all users")
        print(f"{F_YELLOW}4{F_RESET}. Back to main menu")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("add"):
            user_add()
        elif menu_input == "2" or menu_input.startswith("view"):
            user_search("Which user would you like to view? ", True)
        elif menu_input == "3" or menu_input.startswith("display"):
            user_display_all()
        elif menu_input == "4" or menu_input.startswith("back"):
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

def menu_author_operations():
    '''
    Display and handle author menu operations.
    '''
    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}Author Operations:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Add a new author")
        print(f"{F_YELLOW}2{F_RESET}. View author details")
        print(f"{F_YELLOW}3{F_RESET}. Display all authors")
        print(f"{F_YELLOW}4{F_RESET}. Back to main menu")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("add"):
            author_add("")
        elif menu_input == "2" or menu_input.startswith("view"):
            author_details()
        elif menu_input == "3" or menu_input.startswith("display"):
            author_display_all()
        elif menu_input == "4" or menu_input.startswith("back"):
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

# --- Book Operation Functions --- #

def book_add():
    '''
    Add a book to the library, via the Books SQL table.
    '''
    
    print()

    # get valid book title
    while True:
        book_title = input("What is the title of the book? ")
        if re.search(r"^(?!\s*$).+", book_title):
            break
        print("Error: Book title cannot be empty. Book title was not set.")

    # get valid book author
    while True:
        book_author = input("Who is the author of this book? ")
        if re.search(r"^[A-Za-z][A-Za-z\.\-\&+\s]+[A-Za-z]$", book_author):
            # TO-DO: search Authors table for matching author and set author_id equal to Authors.author_id; if not found, create new author, set author_id accordingly
            book_author_id = author_find_or_add(book_author)
            break
        print("Error: Author name must begin and end with letters, and cannot include numbers or special characters other than the following: . - & + ")

    # get valid book isbn
    while True:
        book_isbn = input("What is the ISBN for this book? ")
        isbn_ignore_dashes = str(book_isbn).replace("-", "")
        if re.search(r"^(978|979)[\d]{10}$", isbn_ignore_dashes):
            break
        print("Error: ISBN must be 13 digits and begin with either 978 or 979.")

    # get valid book genre
    while True:
        book_genre = input("What genre is this book? ")
        if re.search(r"^[A-Za-z][A-Za-z\-\&+\s]+[A-Za-z]$", book_genre):
            break
        print("Error: Genre field must begin and end with letters, and cannot include numbers or special characters other than the following: - & + ")

    # get valid publication date
    while True:
        book_pub_date = input("What is the date this book was published? (YYYY-MM-DD) ")
        if re.search(r"^\d{4}\-\d{2}\-\d{2}$", book_pub_date):
            break
        print("Error: Publication date must be in format YYYY-MM-DD")

    # create new book
    Book(book_title, book_author_id, book_isbn, book_genre, book_pub_date)
    author_add_book_to_works(book_author_id, book_title)

def book_format_from_tuple(book_tuple, show_all):
    '''
    Take tuple from Books SQL table and format in user-friendly text block
    '''
    # display all details for given book
    print(f"\nTitle: {F_GREEN}{book_tuple[1]}{F_RESET}")
    print(f"Author: {author_get_name(book_tuple[2])}")   
    if show_all:
        print(f"ISBN: {book_tuple[3]}")
        print(f"Genre: {book_tuple[4]}")
        print(f"Publication Date: {book_tuple[5]}")
        if book_tuple[6] == 1:
            print("Availability Status: Available")
        else:
            print("Availability Status: Currently Unavailable")
            # print(f"Borrowed by Library ID: {book_tuple[7]}")

def book_search(prompt):
    '''
    Search through book tiles and return like titles.
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # search for book to borrow
        search_input = input(f"\n{prompt}")
        search_term = f"%{search_input}%"

        # search Books titles for search term
        query = "SELECT * FROM Books WHERE title LIKE %s"
        cursor.execute(query, (search_term, ))
        results = cursor.fetchall()

        # check through book titles, return if correct book is found
        for result in results:
            while True:
                book_format_from_tuple(result, False)
                menu_input = input("Is this the book you are looking for? ").casefold()
                if menu_input == "yes":
                    return result
                elif menu_input == "no":
                    break
                else:
                    print("Invalid input. Please select \"yes\" or \"no\"")

        # book title was not found
        print(f"\nNo book found with search term \"{search_input}\"")
        return None

    # error handling
    except Exception as e:
        print(f"Error in book_search(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

def book_search_from_menu():
    '''
    Search for books and display details
    '''
    # find book to borrow
    book_to_search = book_search("Which book are you searching for? ")
    if book_to_search == None:
        return
    else:
        print("\nGreat! Here is that book: ")
        book_format_from_tuple(book_to_search, True)

def book_borrow():
    '''
    Prompt user for book to borrow. If available, the book can be loaned out to a user.
    '''
    
    # find book to borrow
    book_to_borrow = book_search("Which book is being checked out? ")
    if book_to_borrow == None:
        return
    # check availability
    elif book_to_borrow[6] == 0:
        print("This book is not available to borrow. Sorry for the inconvenience!")
    else:
        # get user for loan
        user_to_borrow = user_search("Which user would like to borrow this book? ", False)
        if user_to_borrow == None:
            return
        else:
            # connect to database
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                # set book as unavailable
                query = "UPDATE Books SET is_available = 0 WHERE book_id = %s"
                cursor.execute(query, (book_to_borrow[0], ))

                # set borrower to user id
                query = "UPDATE Books SET borrower_id = %s WHERE book_id = %s"
                cursor.execute(query, (user_to_borrow[0], book_to_borrow[0]))

                # get current borrowed_books text
                query = "SELECT borrowed_books FROM Library_Users WHERE user_id = %s"
                cursor.execute(query, (user_to_borrow[0], ))
                current_books = cursor.fetchone()[0]

                # set new borrowed_books text
                if current_books == None:
                    new_books = book_to_borrow[1]
                else:
                    new_books = current_books + ", " + book_to_borrow[1]

                # update with new list of borrowed books
                query = "UPDATE Library_Users SET borrowed_books = %s WHERE user_id = %s"
                cursor.execute(query, (new_books, user_to_borrow[0]))

                conn.commit()

            # error handling
            except Exception as e:
                print(f"Error in book_borrow(): {e}")

            else:
                print(f"\n\"{book_to_borrow[1]}\" has been loaned out to {user_to_borrow[1]}!")
            
            # close connection
            finally:
                cursor.close()
                conn.close()

def book_return_submenu():
    '''
    Return a borrowed book to the library.
    '''
    # find book to return
    book_to_return = book_search("Which book is being returned? ")
    if book_to_return == None:
        return
    # check availability
    elif book_to_return[6] == 1:
        print("This book is already available to borrow. It may have already been returned.")
    else:
        # connect to database
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            # fetch user from borrower id
            query = "SELECT * FROM Library_Users WHERE user_id = %s"
            cursor.execute(query, (book_to_return[7], ))
            user_to_return = cursor.fetchone()

            # set book as available
            query = "UPDATE Books SET is_available = 1 WHERE book_id = %s"
            cursor.execute(query, (book_to_return[0], ))

            # set borrower to null
            query = "UPDATE Books SET borrower_id = %s WHERE book_id = %s"
            cursor.execute(query, (None, book_to_return[0]))

            # remove title from borrowed_books list of user
            query = "SELECT borrowed_books FROM Library_Users WHERE user_id = %s"
            cursor.execute(query, (user_to_return[0], ))
            current_books = cursor.fetchone()[0]

            # remove borrowed book and comma where appropriate
            new_books = current_books.replace(book_to_return[1], "")
            if re.search(r"^,\s|,\s$", new_books):
                new_books = new_books.replace(", ", "")
            elif re.search(r",\s,", new_books):
                new_books = new_books.replace(", ,", ",")
            # elif re.search(r",\s$", new_books):
            #     new_books = new_books.replace(", ", "")
            if new_books == "":
                new_books = None

            query = "UPDATE Library_Users SET borrowed_books = %s WHERE user_id = %s"
            cursor.execute(query, (new_books, user_to_return[0]))

            conn.commit()

        # error handling
        except Exception as e:
            print(f"Error in book_return(): {e}")

        else:
            print(f"\n\"{book_to_return[1]}\" has been returned by {user_to_return[1]}!")
        
        # close connection
        finally:
            cursor.close()
            conn.close()

def book_display_all():
    '''
    Display all books in the library.
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # get list of all books
        query = "SELECT * FROM Books"
        cursor.execute(query)
        books = cursor.fetchall()

        # display contents of library
        if len(books) == 0:
            print("There are no books in your library! Please add some books.")
        else:
            print(f"\n{F_GREEN}Here are all of the books in this library system:{F_RESET}")
            for row in books:
                book_format_from_tuple(row, True)

    # error handling
    except Exception as e:
        print(f"Error in book_display_all(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

# --- User Operation Functions --- #

def user_add():
    '''
    Add a user to the library system.
    '''
    print()

    # get valid user name
    while True:
        user_name = input("What is the new user's name? ")
        if re.search(r"^[A-Za-z][A-Za-z\.\-\s]+[A-Za-z]$", user_name):
            break
        print("Error: Name field must begin and end with letters, and cannot include numbers or special characters other than the following: . -")
    
    # create new user
    User(user_name)

def user_format_from_tuple(user_tuple, show_all):
    '''
    Take tuple from Users SQL table and format in user-friendly text block
    '''
    # display all details for given user
    print(f"\nName: {F_GREEN}{user_tuple[1]}{F_RESET}")
    print(f"Library ID: {str(user_tuple[0]).zfill(8)}")   
    if show_all:
        print(f"Borrowed Books: {user_tuple[2]}")

def user_search(prompt, display_details):
    '''
    Search through users and show all user info if user found.
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # search for author
        search_input = input(f"\n{prompt} ")
        search_term = f"%{search_input}%"

        # search Library_Users SQL table for search term
        query = "SELECT * FROM Library_Users WHERE user_name LIKE %s"
        cursor.execute(query, (search_term, ))
        results = cursor.fetchall()

        # check through user names
        for result in results:
            while True:
                user_format_from_tuple(result, False)
                menu_input = input("Is this the user you are looking for? ").casefold()
                if menu_input == "yes":
                    if display_details:
                        print(f"\nGreat! Here are all the details we have for {result[1]}:")
                        user_format_from_tuple(result, True)
                    return result
                elif menu_input == "no":
                    break
                else:
                    print("Invalid input. Please select \"yes\" or \"no\"")

        # book title was not found
        print(f"\nNo user found with search term \"{search_input}\"")
        return None

    # error handling
    except Exception as e:
        print(f"Error in author_details(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

def user_display_all():
    '''
    Display all users in the library system.
    '''

    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # fetch all user data
        query = "SELECT * FROM Library_Users"
        cursor.execute(query)
        
        for row in cursor.fetchall():
            # display data for given user
            user_format_from_tuple(row, True)

    # error handling
    except Exception as e:
        print(f"Error: {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

# --- Author Operation Functions --- #

def author_add(name):
    '''
    Add an author to the library system using user input.
    '''

    # get valid author name
    if name == "":
        print()
        while True:
            author_name = input("What is the author's name? ")
            if re.search(r"^[A-Za-z][A-Za-z\.\-\&+\s]+[A-Za-z]$", author_name):
                break
            print("Error: Author name must begin and end with letters, and cannot include numbers or special characters other than the following: . - & + ")
    else:
        author_name = name

    # get biography
    biography = input(f"Enter a biography for {author_name}: ")
    
    # create new author
    Author(author_name, biography)

def author_details():
    '''
    Search through authors and show all author info if author found.
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # search for author
        search_input = input(f"\nWhich author would you like to view? ")
        search_term = f"%{search_input}%"

        # search Authors SQL table for search term
        query = "SELECT * FROM Authors WHERE author_name LIKE %s"
        cursor.execute(query, (search_term, ))
        results = cursor.fetchall()

        # check through author names
        for result in results:
            while True:
                author_format_from_tuple(result, False)
                menu_input = input("Is this the author you are looking for? ").casefold()
                if menu_input == "yes":
                    print(f"\nGreat! Here are all the details we have for {result[1]}:")
                    author_format_from_tuple(result, True)
                    return result
                elif menu_input == "no":
                    break
                else:
                    print("Invalid input. Please select \"yes\" or \"no\"")

        # book title was not found
        print(f"\nNo author found with search term \"{search_input}\"")
        return None

    # error handling
    except Exception as e:
        print(f"Error in author_details(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

def author_display_all():
    '''
    Display all authors in the Authors SQL table.
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # fetch all author data
        query = "SELECT * FROM Authors"
        cursor.execute(query)
        
        # display data for every author
        for row in cursor.fetchall():
            author_format_from_tuple(row, True)

    # error handling
    except Exception as e:
        print(f"Error in author_display_all(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

def author_find_or_add(search_name):
    '''
    If author name is in Authors SQL table, return author id. Otherwise, create author and return that id!
    '''

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # fetch user_name using user_id
        query = "SELECT author_id FROM Authors WHERE author_name = %s"
        # search_name = str(search_name).title()
        author_name = (search_name, )
        cursor.execute(query, author_name)
        search_result = cursor.fetchall()

        # if list is empty add new author
        if search_result == []:
            author_add(search_name)
            author_id = author_find_or_add(search_name)
        else:
            author_id = search_result[0][0]

        # Coder's Note: This does not account for multiple authors of the same name. If I had more time I would add code to handle this!

    # error handling
    except Exception as e:
        print(f"Error in author_find_or_add(): {e}")

    # return author id
    else:
        return author_id
    
    # close connection
    finally:
        cursor.close()
        conn.close()

def author_get_name(author_id):
    '''
    Get author's name from given id.
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # fetch all author data
        query = "SELECT author_name FROM Authors WHERE author_id = %s"
        cursor.execute(query, (author_id, ))
        
        # return name from given id
        return cursor.fetchone()[0]

    # error handling
    except Exception as e:
        print(f"Error in author_get_name(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

def author_format_from_tuple(author_tuple, show_all):
    '''
    Take tuple from Author SQL table and format in user-friendly text block
    '''
    # display all details for given user
    print(f"\nAuthor Name: {F_GREEN}{author_tuple[1]}{F_RESET}")
    if show_all:
        print(f"Biography: {author_tuple[2]}")  
        print(f"Works in Library: {author_tuple[3]}")

def author_add_book_to_works(author_id, book_title):
    '''
    Add book title to list of works the author has in library
    '''
    # connect to database
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # get current works_in_library text
        query = "SELECT works_in_library FROM Authors WHERE author_id = %s"
        cursor.execute(query, (author_id, ))
        current_works = cursor.fetchone()[0]

        # set new works_in_library text
        if current_works == None:
            new_works = book_title
        else:
            new_works = current_works + ", " + book_title

        query = "UPDATE Authors SET works_in_library = %s WHERE author_id = %s"
        cursor.execute(query, (new_works, author_id))
        conn.commit()

    # error handling
    except Exception as e:
        print(f"Error in author_add_book_to_works(): {e}")
    
    # close connection
    finally:
        cursor.close()
        conn.close()

# Computer, run program!
print("\nWelcome to the Library Management System!")
menu_main()