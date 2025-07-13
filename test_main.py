import unittest
from main import is_odd

class TestIsOdd(unittest.TestCase):
    def test_odd_number(self):
        self.assertTrue(is_odd(3))

    def test_even_number(self):
        self.assertFalse(is_odd(4))

if __name__ == '__main__':
    unittest.main()

