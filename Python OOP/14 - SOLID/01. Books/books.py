from typing import List

class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books) -> None:
        self.books: List[Book] = books
        
        
    def add_book(self, book: Book):   
        self.books.append(book)
        