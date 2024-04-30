from random import choice
import string


class Account:
    def __init__(self, initial_balance=0):
        self.identifier = self._create_identifier()
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError(f"Not enough money in your account:{self.identifier}")
        self.balance -= amount

    @staticmethod
    def _create_identifier():
        letters_and_digits = string.ascii_letters + string.digits
        # string.ascii_letters+string: retrieves all alphabet letters
        # string.digits: retrieve all digit from 0 to 9
        return "".join([choice(letters_and_digits) for _ in range(25)])
        # The return above will create and generate randomly:unique identifier with 25 characters
