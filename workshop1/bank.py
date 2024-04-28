class Account:
    def __init__(self, identifier, balance=0):
        self.identifier = identifier
        #if balance < 0:
           # raise ("Balance can t be negative")
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
