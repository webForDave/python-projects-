class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for library_book in self.books:
            if library_book.title == book.title and library_book.author == book.author:
                self.books.remove(library_book)
                break  # Exit loop after removing to avoid errors

    def search_books(self, search_string):
        """Search for books by title or author (case insensitive)."""
        matches = []
        search_string = search_string.lower()  # Case insensitive search
        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                matches.append(book)
        return matches


book1 = Book('The Wizard', 'Dave')
books = Library("Dave's library")

books.add_book(book1)

print(books.books)