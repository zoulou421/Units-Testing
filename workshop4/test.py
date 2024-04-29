import pytest

from main import add


def test_add_two_positive_numbers():
    assert add(1, 2) == 3


def test_add_two_letters():
    assert add("a", "b") == "ab"


def test_add_two_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, True) == 1
    assert add(False, False) == 0


def test_add_two_None_v2():
    with pytest.raises(TypeError):  # context manager
        add(None, None)
