class Genre:
    name: str
    books: list

    def __init__(self, name: str):
        self.name = name
        self.books = []

    def __repr__(self):
        return f'{self.name}'

    def __eq__(self, other):
        return isinstance(other, Genre) and self.name == other.name

    def add_book(self, book):
        self.books.append(book)
        print(book, "добавлена в жанр", self.name)


class User:
    __name: str
    __id: int
    books: list

    def __init__(self, name: str, id: int):
        self.__name = name
        self.__id = id
        self.books = []

    def get_id(self):
        return self.__id

    # Геттер
    def get_name(self):
        return self.__name

    # Сеттер
    def change_name(self, new_name: str):
        bad_words = ['дурак']
        if isinstance(new_name, str) and new_name.lower() not in bad_words:
            self.__name = new_name

    # Ещё геттер
    @property
    def name(self):
        return self.__name

    # Ещё сеттер
    @name.setter
    def name(self, new_name):
        self.change_name(new_name)

    def add_book(self, book):
        self.books.append(book)
        print(book, "взята пользователем", self.__id)

    def return_book(self, book):
        self.books.append(book)
        print(book, "отдана пользователем", self.__id)

    def list_of_unreturned_books(self):
        books_set = set(self.books)
        for i in books_set:
            if self.books.count(i) % 2 != 0:
                print(i)


class Book:
    name: str
    __text: str
    authors: list
    genre: list[Genre]
    __users: list[User]

    def __init__(self, name: str, text: str, authors: list, genre: list[Genre]):
        self.name = name
        self.__text = text
        self.authors = authors
        self.genre = genre
        self.__users = []

    def __repr__(self):
        return f'{self.name} {self.authors} {self.genre}'

    def read(self):
        return self.__text

    def add_user(self, user: User):
        self.__users.append(user)


genre = Genre("Фантастика")
genre2 = Genre("Фантастика")

print(genre == genre2)

# genre_2 = Genre("Детектив")
# genre_2.add_book("Шерлок Холмс")
# genre.add_book("Гарри Поттер")

garry = Book("Гарри Поттер", "Высоко-высоко в горах...", [], [genre])

garry.__text = "А тут ничего нет"

print(garry.__text)
print(garry.read())

user = User("Георгий", 1)
user.add_book("Шерлок Холмс")
user.return_book("Шерлок Холмс")
user.add_book("Шерлок Холмс")
user.list_of_unreturned_books()

user.change_name(['Фамилия', 'Имя', 'Отчество'])
user.change_name('ДУРАК')
print(user.name)

user.name += ' Петров'
# user.name = user.name + 'Петров'
print(user.name)

user.name = 'Дурак'
print(user.name)

garry.add_user(user)
