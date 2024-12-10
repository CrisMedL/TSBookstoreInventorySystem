DROP DATABASE IF EXISTS bookstore;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

/* 
 * All IDs should be unsigned for consistency across tables. 
 */

/*
 * The `genres` table stores unique book genres. 
 * The genre_name is set to be unique and cannot be null.
 */
CREATE TABLE IF NOT EXISTS genres(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL UNIQUE
);

/*
 * The `authors` table stores details of book authors, including their first and last names.
 */
CREATE TABLE IF NOT EXISTS authors(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    author_full_name VARCHAR(100) NOT NULL
);

/*
 * The `books` table stores details of books available in the bookstore.
 * Each book must be associated with a genre and an author.
 * If a genre or author is deleted, all associated books will also be deleted automatically.
 */
CREATE TABLE IF NOT EXISTS books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    # utf8 is the character set, 
    # general is the collation type (comparing strings)
    # ci is for case-insensitive
    title VARCHAR(255) COLLATE utf8mb4_general_ci NOT NULL UNIQUE,
    genre_id INT UNSIGNED NOT NULL ,
    author_id INT UNSIGNED NOT NULL,
    price DECIMAL(10, 2) NOT NULL ,
    stock_quantity INT NOT NULL ,
    FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE RESTRICT,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE RESTRICT
);	

