from library_sql.sql_ops import connect_to_db

# originally a class to create library user objects; now the init passes the object through to the SQL database!
class User:

    def __init__(self, name):
        self._name = name

        # connect to database
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            # insert new user into Library_User table
            values = (self._name, )
            query = "INSERT INTO Library_Users (user_name) VALUES (%s)"
            cursor.execute(query, values)
            conn.commit()
            print(f"{self._name} has been added to the library system!")

        # error handling
        except Exception as e:
            print(f"Error in User __init__: {e}")
        
        # close connection
        finally:
            cursor.close()
            conn.close()