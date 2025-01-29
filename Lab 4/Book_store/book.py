class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"
    
    def discount(self, percentage):
        self.price -= self.price * (percentage / 100)
    
    def get_details(self):
        return f"Title: {self.title}, Author: {getattr(self, 'author', 'N/A')}, Price: {self.price:.2f} BDT"

my_book = Book("Amar Ache Jol", "Humayun Ahmed", 250)
print(my_book)

my_book.discount(10)
print(my_book.get_details())

my_book.price = 190
print(my_book.get_details())

del my_book.author
print(my_book.get_details())


del my_book
