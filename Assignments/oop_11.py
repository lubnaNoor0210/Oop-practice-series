# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self,title,author):
        self.title= title
        self.author = author
        Book.increment_book_count()

    @classmethod

    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("Anne of green gables" , "Roald Dahl")
book2 = Book("CHarlie and the chocolate factory", "Roald Dahl")
print("Total books created:", Book.total_books)