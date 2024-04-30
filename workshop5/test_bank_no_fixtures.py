from account import Account


# Testing without Fixtures

def test_deposit():
    account = Account(initial_balance=1000)
    account.deposit(amount=3000)
    assert account.balance == 4000


def test_withdraw():
    account = Account(initial_balance=1000)
    account.withdraw(amount=500)
    assert account.balance == 500


def test_create_identifier_len():
    account = Account(initial_balance=1000)
    assert len(account.identifier) == 25


def test_create_identifier_isalnum():
    account = Account(initial_balance=1000)
    assert account.identifier.isalnum() is True
