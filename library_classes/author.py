from library_sql.sql_ops import connect_to_db

# originally a class to create author objects; now the init passes the object through to the SQL database!
class Author:

    def __init__(self, name, biography):
        self._name = name
        self._biography = biography
        # self._books_in_library = []

        # connect to database
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            # insert new user into Library_User table
            values = (self._name, self._biography)
            query = "INSERT INTO Authors (author_name, biography) VALUES (%s, %s)"
            cursor.execute(query, values)
            conn.commit()
            print(f"{self._name} has been added to the library system!")

        # error handling
        except Exception as e:
            print(f"Error in Author __init__(): {e}")
        
        # close connection
        finally:
            cursor.close()
            conn.close()