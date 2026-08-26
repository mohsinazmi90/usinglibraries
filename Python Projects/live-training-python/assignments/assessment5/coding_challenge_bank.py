# 12. *Bank Account system* banao:
# * deposit
# * withdraw
# * balance
# * transaction history

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history
    
# Example usage:
account = BankAccount("John Doe")
account.deposit(1000)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")
print("Transaction History:")

for transaction in account.get_transaction_history():
    print(transaction)
    


