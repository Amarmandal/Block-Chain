# Importing the unittest module from the Python Standard Library
import unittest
# Importing the prime_generator module
from lib.prime_generator import *

# Defining the TestGenerateRandomPrime class as a subclass of unittest.TestCase
class TestGenerateRandomPrime(unittest.TestCase):
    # Defining the test_generate_random_prime method to test the generate_random_prime function
    def test_generate_random_prime(self):
        # Defining the start and end values for generating a random prime number
        start, end = 1, 20
        # Calling the generate_random_prime function and storing the result in the variable "result"
        result = generate_random_prime(start, end)
        # Asserting that the result is greater than or equal to the start value
        self.assertTrue(result >= start)
        # Asserting that the result is less than or equal to the end value
        self.assertTrue(result <= end)
        # Asserting that the result is a prime number using the is_prime function
        self.assertTrue(is_prime(result))

# The main function is executed only when the module is run as a standalone program
if __name__ == '__main__':
    # Calling the unittest.main function to run the tests defined in the TestGenerateRandomPrime class
    unittest.main()
