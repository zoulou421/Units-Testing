from bank import Account
import pytest


def test_account_in_creation():
    account1 = Account(identifier="000", balance=1000)
    # account2 = Account(identifier="000", balance=-1000)

    assert account1.balance == 1000
    # assert account2.balance == -1000
    with pytest.raises(ValueError):
        account2 = Account(identifier="000", balance=-1000)
