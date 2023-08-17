# main.py
from book import Book
from patron import Patron

def main():
    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Create patrons
    patron1 = Patron("Alice")
    patron2 = Patron("Bob")

    # Check out books
    patron1.check_out(book1)
    patron1.check_out(book2)
    patron2.check_out(book2)
    patron2.check_out(book3)

    # Print book and patron info
    print(book1)
    print(book2)
    print(book3)
    print(patron1)
    print(patron2)

    # Return books
    patron1.return_book(book1)
    patron2.return_book(book2)

    # Print updated patron info
    print(patron1)
    print(patron2)

if __name__ == "__main__":
    main()
