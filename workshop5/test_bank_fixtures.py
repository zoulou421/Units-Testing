from account import Account

# Testing with Fixtures
import pytest


@pytest.fixture
def my_account():
    return Account(initial_balance=1000)


def test_deposit(my_account):
    my_account.deposit(amount=3000)
    assert my_account.balance == 4000


def test_withdraw(my_account):
    my_account.withdraw(amount=500)
    assert my_account.balance == 500


# sometime you can do this:
def test_withdraw_enough_money():
    account = Account(initial_balance=400)
    with pytest.raises(ValueError):
        account.withdraw(amount=500)


def test_create_identifier_len(my_account):
    assert len(my_account.identifier) == 25


def test_create_identifier_isalnum(my_account):
    assert my_account.identifier.isalnum() is True
