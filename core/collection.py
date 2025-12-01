from .book import Book

class Collection:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)

    def __repr__(self):
        return f'{self.__name} (всего книг: {len(self.__books)})'
