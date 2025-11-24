class Book:
    def __init__(self, name, text, authors, genre):
        self.name = name
        self.__text = text
        self.authors = authors
        self.genre = genre
        self.__users = []

    def __repr__(self):
        return f'{self.name} {self.authors} {self.genre}'

    def read(self):
        return self.__text

    def add_user(self, user):
        self.__users.append(user)
