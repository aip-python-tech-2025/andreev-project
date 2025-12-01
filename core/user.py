class User:
    def __init__(self, name, user_id):
        self._name = name
        self._id = user_id
        self.books = []

    def get_id(self):
        return self._id

    # Геттер
    def get_name(self):
        return self._name

    def __repr__(self):
        return f'{self._name} (ID: {self._id})'

    # Сеттер
    def change_name(self, new_name: str):
        bad_words = ['дурак']
        if isinstance(new_name, str) and new_name.lower() not in bad_words:
            self._name = new_name

    # Ещё геттер
    @property
    def name(self):
        return self._name

    # Ещё сеттер
    @name.setter
    def name(self, new_name):
        self.change_name(new_name)

    def add_book(self, book):
        self.books.append(book)
        print(book, "взята пользователем", self._id)

    def return_book(self, book):
        self.books.append(book)
        print(book, "отдана пользователем", self._id)

    def list_of_unreturned_books(self):
        books_set = set(self.books)
        for i in books_set:
            if self.books.count(i) % 2 != 0:
                print(i)
