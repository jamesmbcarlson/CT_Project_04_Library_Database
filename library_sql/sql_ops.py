import mysql.connector

def connect_to_db():

    # attempt to connect to database
    try:
        conn = mysql.connector.connect(
            database = "library_db",
            user ="root",
            password = "Password123!",
            host = "localhost"
        )

        # return connection if successful
        # print("Connected Successfully to Library Database")
        return conn
    
    # connection failed; inform user
    except mysql.connector.Error as e:
        print(f"Error: {e}")