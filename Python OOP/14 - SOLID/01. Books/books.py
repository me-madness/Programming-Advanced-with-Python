from typing import List

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page
        
        
    def __repr__(self) -> str:
        return f"Title {self.title} by {self.author}"    


class Library:
    def __init__(self, books) -> None:
        self.books: list[Book] = books
        
        
    def add_book(self, book: Book):   
        self.books.append(book)
        
        
    def remove_book(self, title):
        to_remove = [b for b in self.books if b.title == title]    
        
        if not to_remove:
            raise ValueError("No such title")
        
        if len(to_remove) > 1:
            raise ValueError("Too many books were found")
        
        self.books.remove(to_remove[0])
        
        
    def get_books_by_author(self, author):
        return [b for b in self.books if b.author == author]
    
    
    def get_books_by_title(self, title):    
        books = [b for b in self.books if b.title == title]
        
        if not books:
            raise ValueError("No such title")
        
        return books
    
    
if __name__ == "__main__":
    book = Book("1", "a")    
    book2 = Book("2", "b")    
    book3 = Book("3", "c")    
    
    lib = Library([book, book2, book3])
    
    print(lib.get_books_by_title("1"))
    print(lib.get_books_by_author("a"))
    book4 = Book("4", "d")
    
    lib.add_book(book4)
    
    print(lib.get_books_by_title("4"))
    
    print(lib.get_books_by_author("5"))
    # print(lib.get_books_by_title("non"))   