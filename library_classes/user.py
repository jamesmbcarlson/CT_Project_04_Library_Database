import re
from library_sql.sql_ops import connect_to_db

# A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
class User:
    # def __init__(self):
    #     self._name = None
    #     self.__library_id = None
    #     self._borrowed_books = []

    def __init__(self, name):
        self._name = name

        # connect to database
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            # insert new user into Library_User table
            values = (self.get_name(), )
            query = "INSERT INTO Library_User (user_name) VALUES (%s)"
            cursor.execute(query, values)
            conn.commit()
            print(f"{self.get_name()} has been added to the library system!")

        # error handling
        except Exception as e:
            print(f"Error: {e}")
        
        # close connection
        finally:
            cursor.close()
            conn.close()

    # getters and setters
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if re.search(r"^[A-Za-z][A-Za-z\.\-\s]+[A-Za-z]$", new_name):
            self._name = new_name
        else:
            print("Error: Name field must begin and end with letters, and cannot include numbers or special characters other than the following: . -")

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_id):
        # sets user id to 8 digit identifier
        self.__library_id = str(new_id).zfill(8)

    def get_borrowed_books(self):
        return self._borrowed_books
    
    def set_borrowed_books(self, list_of_books):
        self._borrowed_books = list_of_books

    def add_to_borrowed_books(self, book):
        self._borrowed_books.append(book)

    def remove_from_borrowed_books(self, book):
        self._borrowed_books.remove(book)