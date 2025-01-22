customers = []

def add_customer(name, email, phone):
    customers.append({'name': name, 'email': email, 'phone': phone})

def list_customers():
    if not customers:
        print("No customers available.")
    else:
        for customer in customers:
            print(f"Name: {customer['name']}, Email: {customer['email']}, Phone: {customer['phone']}")
