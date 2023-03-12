class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
	else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")

    def customer_details(self):
        print(f"Account number: {self.account_number}")
        print(f"Customer name: {self.customer_name}")
        print(f"Date of opening: {self.date_of_opening}")
        print(f"Current balance: {self.balance}")