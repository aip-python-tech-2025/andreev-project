class Book:
    def __init__(self, name, text, authors, genre):
        self.name = name
        self.__text = text
        self.authors = authors
        self.genre = genre
        self.__users = []

    def __repr__(self):
        authors = ", ".join([str(a) for a in self.authors])
        genres = ", ".join([str(a) for a in self.genre])
        return f'{self.name}\nАвторы: {authors}\nЖанры: {genres}'

    def read(self):
        return self.__text

    def add_user(self, user):
        self.__users.append(user)
