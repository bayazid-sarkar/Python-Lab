orders = []

def place_order(customer_name, book_title, quantity):
    orders.append({'customer_name': customer_name, 'book_title': book_title, 'quantity': quantity})

def list_orders():
    if not orders:
        print("No orders placed.")
    else:
        for order in orders:
            print(f"Customer: {order['customer_name']}, Book: {order['book_title']}, Quantity: {order['quantity']}")
