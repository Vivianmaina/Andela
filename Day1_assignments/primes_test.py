import unittest
from primes import generate_primes

class TestGeneratePrimesMethod(unittest.TestCase):
    def test_correctresult(self): #Tests if result is a prime
        self.assertEqual(generate_primes(10), [2,3,5,7])

    def test_less_than_two(self):
        self.assertEqual(generate_primes(1), 'No prime number below 2')

    def test_number_one(self):  # Tests the result does not include 1.
        self.assertNotIn(1, generate_primes(10))

    def test_not_zero(self):  # Tests the input should not be zero.
        with self.assertRaises(ValueError):
            generate_primes(0)

    def test_negative_number(self):   # Tests the input should not be negative
        self.assertEqual(generate_primes(-5), 'Negative numbers cannot be prime numbers')

    def test_stringInput(self):  # Tests the input should not be of string type
        self.assertEqual(generate_primes('two'), 'Cannot find prime of non integer')

    def test_isnot_float(self):  # Tests if float and raise a ValueError.
        with self.assertRaises(TypeError):
            generate_primes(4.5)

   


if __name__ == '__main__':
    unittest.main()

