from core.book import Book
from core.genre import Genre
from core.user import User


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
