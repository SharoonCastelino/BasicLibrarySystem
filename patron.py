# patron.py

class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_books = []

    def check_out(self, book):
        if book.checkout():
            self.checked_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.checked_books and book.return_book():
            self.checked_books.remove(book)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} has {len(self.checked_books)} books checked out."
