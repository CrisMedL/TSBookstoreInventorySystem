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

CREATE TABLE IF NOT EXISTS discounts (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    discount_name VARCHAR(100) NOT NULL,  -- e.g., "10% Discount", "Black Friday Sale"
    discount_percentage DECIMAL(5,2) NOT NULL CHECK (discount_percentage >= 0 AND discount_percentage <= 100)
);

/*
 * The `books` table stores details of books available in the bookstore.
 * Each book must be associated with a genre and an author.
 * If a genre or author is deleted, all associated books will also be deleted automatically.
 */
CREATE TABLE IF NOT EXISTS books(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre_id INT UNSIGNED NOT NULL,
    author_id INT UNSIGNED NOT NULL,
    original_price DECIMAL(8,2) NOT NULL,
    discount_price DECIMAL(8,2) NULL,
    has_discount  TINYINT NULL DEFAULT 0,
    discount_id INT UNSIGNED NULL,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE,
    FOREIGN KEY (discount_id) REFERENCES discounts(id) ON DELETE SET NULL  -- Ensures books without a discount aren't left with invalid data
);

/*
 * The `book_logs` table tracks administrative actions related to books.
 * Each log entry records the book affected, the action type, and additional details.
 * If a book is deleted, all related log entries will also be deleted automatically. Couldn't find a better way to do this \(-.-)/
 */
CREATE TABLE IF NOT EXISTS book_logs(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    book_id INT UNSIGNED NOT NULL,
    action_details TEXT NOT NULL, -- Detailed description of the action for management purposes
    action_occurred_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id) 
    );