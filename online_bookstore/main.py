from book import add_book, list_books
from customer import add_customer, list_customers
from order import place_order, list_orders

while True:
    print("\nOnline Bookstore Management")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Add a new customer")
    print("4. List all customers")
    print("5. Place a new order")
    print("6. List all orders")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        price = float(input("Enter book price: "))
        add_book(title, author, genre, price)
        print("Book added successfully.")
    elif choice == 2:
        list_books()
    elif choice == 3:
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        add_customer(name, email, phone)
        print("Customer added successfully.")
    elif choice == 4:
        list_customers()
    elif choice == 5:
        customer_name = input("Enter customer name: ")
        book_title = input("Enter book title: ")
        quantity = int(input("Enter quantity: "))
        place_order(customer_name, book_title, quantity)
        print("Order placed successfully.")
    elif choice == 6:
        list_orders()
    elif choice == 7:
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")
