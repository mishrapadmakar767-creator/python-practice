
# Python Encapsulation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    # Withdraw Money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Display Balance
    def show_balance(self):
        print("Account Holder:", self.owner)
        print("Balance:", self.__balance)


account = BankAccount("Padmakar", 5000)

account.show_balance()
account.deposit(1000)
account.withdraw(2000)
account.show_balance()
