import requests


class Library:
    @staticmethod
    def get_book_by_isbn(isbn):
        url = f'https://openlibrary.org/search.json?q={isbn}&limit=1'
        data = requests.get(url).json()['docs'][0]
        book_info = {
            'title': data['title'],
            'authors': data['author_name'],
        }
        return book_info
