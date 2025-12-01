from core.author import Author
from core.book import Book
from core.collection import Collection
from core.genre import Genre
from core.librarian import Librarian
from core.user import User

genre = Genre("Фантастика")
author = Author('Джоан Роулинг')
garry_1 = Book("Гарри Поттер и философский камень", "Высоко-высоко в горах...", [author], [genre])
garry_2 = Book("Гарри Поттер и тайная комната", "Глубоко-глубоко под землёй...", [author], [genre])

potter_books = Collection('Гарри Поттер')
potter_books.add_book(garry_1)
potter_books.add_book(garry_2)
print(potter_books)

user = User("Георгий", 1)
user.add_book("Шерлок Холмс")
user.return_book("Шерлок Холмс")
user.add_book("Шерлок Холмс")
user.list_of_unreturned_books()

librarian = Librarian('Геннадий Петрович', [1, 2, 3, 4, 5], 2)
librarian.add_book(garry_1)
print(librarian)

user.change_name(['Фамилия', 'Имя', 'Отчество'])
user.change_name('ДУРАК')
print(user.name)

user.name += ' Петров'
# user.name = user.name + 'Петров'
print(user.name)

user.name = 'Дурак'
print(user.name)

garry_1.add_user(user)
print(user)

for o in genre, author, user, librarian, garry_1, garry_2, potter_books:
    print(o.__repr__())
