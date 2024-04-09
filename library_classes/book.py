import re

# A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
class Book:

    def __init__(self):
        self.__title = None
        self.__author = None
        self.__isbn = None
        self.__genre = None
        self.__publication_date = None
        self._is_available = True
        self.__borrower = None
    
    # getters and setters for all values

    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        if re.search(r"^(?!\s*$).+", new_title):
            self.__title = new_title
        else:
            print("Error: Book title cannot be empty. Book title was not set.")
    
    def get_author(self):
        return self.__author
    
    def set_author(self, new_name):
        if re.search(r"^[A-Za-z][A-Za-z\.\-\&+\s]+[A-Za-z]$", new_name):
            self.__author = new_name
        else:
            print("Error: Author field must begin and end with letters, and cannot include numbers or special characters other than the following: . - & + ")

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, new_isbn):
        isbn_ignore_dashes = str(new_isbn).replace("-", "")
        if re.search(r"^(978|979)[\d]{10}$", isbn_ignore_dashes):
            self.__isbn = new_isbn
        else:
            print("Error: ISBN must be 13 digits and begin with either 978 or 979.")
    
    def get_genre(self):
        return self.__genre
    
    def set_genre(self, new_genre):
        if re.search(r"^[A-Za-z][A-Za-z\-\&+\s]+[A-Za-z]$", new_genre):
            self.__genre = new_genre
        else:
            print("Error: Genre field must begin and end with letters, and cannot include numbers or special characters other than the following: - & + ")
    
    def get_publication_date(self):
        return self.__publication_date
    
    def set_publication_date(self, new_date):
        if re.search(r"^\d{2}/?\-?\d{2}/?\-?\d{4}$", new_date):
            self.__publication_date = new_date
        else:
            print("Error: Publication date must be in format MM/DD/YYYY")
    
    def get_is_available(self):
        return self._is_available
    
    def set_is_available(self, new_status):
        self._is_available = new_status

    def get_borrower(self):
        return self.__borrower
    
    def set_borrower(self, user):
        self.__borrower = user

# book subclasses
class FantasyBook(Book):
    def __init__(self):
        super().__init__()
        self.set_genre("Fantasy")

class SciFiBook(Book):
    def __init__(self):
        super().__init__()
        self.set_genre("Science Fiction")

class NonFictionBook(Book):
    def __init__(self):
        super().__init__()
        self.set_genre("Non-Fiction")