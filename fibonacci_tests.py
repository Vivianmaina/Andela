import unittest

from fibonacci import fib_recursive

class Test_fib_recursive(unittest.TestCase):    # Define which function to test
    def test(self):
        self.assertEqual(0,fib_recursive(0), msg='should return 0 for 0')

    def test(self):
        self.assertEqual(-3,fib_recursive(-3), msg='should return Only positive numbers please')

    def test(self):
        self.assertEqual(5,fib_recursive(5), msg='should return [0,1,1,2,3] for 5')      

