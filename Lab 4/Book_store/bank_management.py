class BankAccount:
    class Transaction:
        def __init__(self, transaction_id, transaction_type, amount, date):
            self.transaction_id = transaction_id
            self.transaction_type = transaction_type
            self.amount = amount
            self.date = date
        
        def __str__(self):
            return f"Transaction ID: {self.transaction_id}, Type: {self.transaction_type}, Amount: BDT{self.amount}, Date: {self.date}"
    
    def __init__(self, account_holder, account_number, balance, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transactions = []
    
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Type: {self.account_type}, Balance: BDT{self.balance:.2f}"
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(self.Transaction(str(len(self.transactions)+1), "Deposit", amount, "2025-01-29"))
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(self.Transaction(str(len(self.transactions)+1), "Withdrawal", amount, "2025-01-29"))
        else:
            print("Insufficient balance")
    
    def get_balance(self):
        return self.balance
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

account1 = BankAccount("Bayazid Sarkar", "123456789", 50000.00, "Current")
print(account1)

print("Deposited Amount:", 20000.00)
account1.deposit(20000.00)

print("Current Balance:", account1.get_balance())

print("Withdrawn Amount:", 10000.00)
account1.withdraw(10000.00)

print("Current Balance after withdrawal:", account1.get_balance())

account1.account_type = "Savings"
print(account1)

del account1.account_number

print("\nTransaction History:")
for transaction in account1.transactions:
    print(transaction)

del account1
