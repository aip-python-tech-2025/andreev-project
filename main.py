from core.author import Author
from core.book import Book
from core.genre import Genre
from core.user import User


genre = Genre("Фантастика")
author = Author('Джоан Роулинг')
garry = Book("Гарри Поттер", "Высоко-высоко в горах...", [author], [genre])

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
