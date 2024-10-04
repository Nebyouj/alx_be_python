class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def display(self):
        print(f"{self.title} by {self.author}")

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"{title} has been checked out.")
                else:
                    print(f"{title} is already checked out.")
                return
        print(f"{title} is not available in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} wasn't checked out.")
                return
        print(f"{title} does not belong to this library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                book.display()
        else:
            print("No books are currently available.")