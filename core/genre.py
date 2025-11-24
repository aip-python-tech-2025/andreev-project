class Genre:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __repr__(self):
        return f'{self.name}'

    def __eq__(self, other):
        return isinstance(other, Genre) and self.name == other.name

    def add_book(self, book):
        self.books.append(book)
        print(book, "добавлена в жанр", self.name)
