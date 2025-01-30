class Library:
    def __init__(self):
        self.books = []
    def addBooks(self,book):
        self.books.append(book)
    def viewBooks(self):
        print("Library has following books:")
        for i,book in enumerate(self.books,1):
            print(f"{i}. {book}")
    def search(self,b):
        for book in self.books:
            if b == book:
                print(f"searched book is found: {book}")
lib  = Library()
lib.addBooks("Hello Python")
lib.addBooks("java")
lib.viewBooks()
lib.search("Hello Python")