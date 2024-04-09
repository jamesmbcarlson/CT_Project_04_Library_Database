CREATE DATABASE library_db;

USE library_db;

CREATE TABLE Books(
	book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    isbn VARCHAR(17) NOT NULL,
    genre VARCHAR(255),
    publication_date DATE,
    is_available BOOLEAN DEFAULT 1,
    borrower_id INT,
    FOREIGN KEY (author_id) REFERENCES Author(author_id),
    FOREIGN KEY (borrower_id) REFERENCES Library_User(user_id)
);

CREATE TABLE Library_User(
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL
);

CREATE TABLE Author(
	author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL,
    biography TEXT
);

SELECT *
FROM Library_User;

SELECT *
FROM Author;