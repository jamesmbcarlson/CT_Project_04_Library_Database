CREATE DATABASE library_db;

USE library_db;

CREATE TABLE Books(
	book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    isbn VARCHAR(17) NOT NULL UNIQUE,
    genre VARCHAR(255),
    publication_date DATE,
    is_available BOOLEAN DEFAULT 1,
    borrower_id INT DEFAULT NULL,
    FOREIGN KEY (author_id) REFERENCES Author(author_id),
    FOREIGN KEY (borrower_id) REFERENCES Library_User(user_id)
);

CREATE TABLE Library_Users(
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL
);

CREATE TABLE Authors(
	author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL,
    biography TEXT
);

SELECT *
FROM Books;

SELECT *
FROM Library_Users;

SELECT *
FROM Authors;

-- RENAME TABLE Library_User TO Library_Users;
-- RENAME TABLE Author TO Authors;

-- ALTER TABLE Library_Users
-- ADD borrowed_books TEXT;

-- ALTER TABLE Authors
-- ADD works_in_library TEXT;

-- UPDATE Authors
-- SET works_in_library = "Elantris"
-- WHERE author_id = 1;

-- UPDATE Authors
-- SET works_in_library = "The Name of the Wind"
-- WHERE author_id = 2;

-- UPDATE Authors
-- SET works_in_library = "Elantris, Mistborn: The Final Empire"
-- WHERE author_id = 1;

-- ALTER TABLE Library_Users
-- MODIFY COLUMN borrowed_books TEXT;

-- UPDATE Books
-- SET is_available = 1
-- WHERE book_id = 1;

-- UPDATE Books
-- SET borrower_id = null
-- WHERE book_id = 1;