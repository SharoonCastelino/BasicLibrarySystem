# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def checkout(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        else:
            return False

    def __str__(self):
        status = "available" if not self.checked_out else "checked out"
        return f"'{self.title}' by {self.author} - {status}"
