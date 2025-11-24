class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__id = user_id
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
