from library.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for author_name, books in self.books_available.items():
            if author == author_name and book_name in books:
                user.books.append(book_name)
                self.books_available[author_name].remove(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        book_info = self.rented_books[user.username][book_name]
        return f'The book "{book_name}" is already rented and will be available in {book_info} days!'

    def return_book(self, author: str, book_name:str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"