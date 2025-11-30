class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   # Private attribute

    # Mark the book as checked out
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    # Mark the book as returned
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    # Check if the book is available
    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # Private list to store Book objects

    # Add a new book to the library
    def add_book(self, book):
        self._books.append(book)

    # Check out a book by title
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    # Return a book by title
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    # List all available books
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
