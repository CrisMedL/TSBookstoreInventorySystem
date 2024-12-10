USE bookstore;

INSERT INTO genres (genre_name)
VALUES 
    ('Fiction'),
    ('Non-Fiction'),
    ('Mystery'),
    ('Fantasy'),
    ('Romance'),
    ('Science Fiction'),
    ('Thriller'),
    ('Young Adult'),
    ('Horror'),
    ('Biography');
    
INSERT INTO authors (author_full_name)
VALUES
    ('Leo Tolstoy'),
    ('Malcolm Gladwell'),
    ('Agatha Christie'),
    ('J.R.R. Tolkien'),
    ('Nicholas Sparks'),
    ('Isaac Asimov'),
    ('Dan Brown'),
    ('J.K. Rowling'),
    ('Stephen King'),
    ('Walter Isaacson');
    
INSERT INTO books (title, genre_id, author_id, price, stock_quantity)
VALUES
    ('War and Peace', 1, 1, 19.99, 8), -- Fiction by Leo Tolstoy
    ('Outliers', 2, 2, 14.99, 13), -- Non-Fiction by Malcolm Gladwell
    ('Murder on the Orient Express', 3, 3, 12.99, 10), -- Mystery by Agatha Christie
    ('The Hobbit', 4, 4, 18.50, 7), -- Fantasy by J.R.R. Tolkien
    ('The Notebook', 5, 5, 9.99, 10), -- Romance by Nicholas Sparks
    ('Foundation', 6, 6, 16.99, 4), -- Science Fiction by Isaac Asimov
    ('The Da Vinci Code', 7, 7, 14.50, 11), -- Thriller by Dan Brown
    ('Harry Potter and the Sorcerer\'s Stone', 8, 8, 22.99, 5), -- Young Adult by J.K. Rowling
    ('The Shining', 9, 9, 15.99, 11), -- Horror by Stephen King
    ('Steve Jobs', 10, 10, 24.99, 6); -- Biography by Walter Isaacson


