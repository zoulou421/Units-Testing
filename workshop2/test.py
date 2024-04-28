from unittest import TestCase

from main import add


class TestCalculator(TestCase):
    def test_add_two_positive_numbers(self):
        self.assertEquals(add(1, 2), 3)