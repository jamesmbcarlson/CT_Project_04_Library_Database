from library_sql.sql_ops import connect_to_db

# originally a class to create book objects; now the init passes the object through to the SQL database!
class Book:

    def __init__(self, title, author_id, isbn, genre, publication_date):
        self.__title = title
        self.__author_id = author_id
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self._is_available = True

        # connect to database
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            # insert new user into Library_User table
            values = (self.__title, self.__author_id, self.__isbn, self.__genre, self.__publication_date)
            query = "INSERT INTO Books (title, author_id, isbn, genre, publication_date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, values)
            conn.commit()
            print(f"{self.__title} has been added to the library system!")

        # error handling
        except Exception as e:
            print(f"Error in Book __init__(): {e}")
        
        # close connection
        finally:
            cursor.close()
            conn.close()