from bank import Account

account1 = Account(identifier="000", balance=1000)
account2 = Account(identifier="000", balance=-1000)

assert account1.balance == 1000
assert account2.balance == -1000
