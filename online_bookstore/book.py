inventory = []

def add_book(title, author, genre, price):
    inventory.append({'title': title, 'author': author, 'genre': genre, 'price': price})

def list_books():
    if not inventory:
        print("No books available.")
    else:
        for book in inventory:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Price: {book['price']}")

