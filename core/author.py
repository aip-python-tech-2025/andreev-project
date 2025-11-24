class Author:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return self.__name

    def get_name(self):
        return self.__name
