from unittest import TestCase

from main import add


class TestCalculator(TestCase):
    def test_add_two_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")  # will not work because  of the condition isinstance in current main.py file

    def test_add_two_booleans(self):
        self.assertEqual(add(True, False), 1)
        self.assertEqual(add(True, True), 2)
        self.assertEqual(add(False, True), 1)
        self.assertEqual(add(False, False), 0)
