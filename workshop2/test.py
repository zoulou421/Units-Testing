from unittest import TestCase
# from unittest import main [ main is not used to compile]

from main import add


class TestCalculator(TestCase):
    def test_add_two_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

##For specific test using main module
# main()
# make a test in terminal:  python workshop2/test.py |  python workshop2/test.py -v(--verbose)

##For specific test not using main module(you can take out [main] module and its [import]):
# without specification: python -m unittests (will test every file in current directory starting with test. example: test_main.py)
# specified:  python -m unittest workshop2/test.py (will only test).

## [N.B:unittest only tests functions or methods of file which starts with prefix :test as above]
# thirdly, you can use the IDE (pycharm for test as usual:run)
