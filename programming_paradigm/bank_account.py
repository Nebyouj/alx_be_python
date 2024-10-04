class BankAccount:
    def __init__(self, account_balance:int):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

