# Importing the unittest module from the Python Standard Library
import unittest
# Importing the generate_key module
from lib.generate_key import *

# Defining the TestRSAFunctions class as a subclass of unittest.TestCase
class TestRSAFunctions(unittest.TestCase):

    # Defining the test_get_gcd method to test the get_gcd function
    def test_get_gcd(self):
        # Asserting that the get_gcd of 24 and 60 is equal to 12
        self.assertEqual(get_gcd(24, 60), 12)
        # Asserting that the get_gcd of 10 and 15 is equal to 5
        self.assertEqual(get_gcd(10, 15), 5)
        # Asserting that the get_gcd of 55 and 121 is equal to 11
        self.assertEqual(get_gcd(55, 121), 11)

    # Defining the test_mod_inverse method to test the mod_inverse function
    def test_mod_inverse(self):
        # Asserting that the mod_inverse of 7 and 26 is equal to 15
        self.assertEqual(mod_inverse(7, 26), 15)
        # Asserting that the mod_inverse of 5 and 26 is equal to 21
        self.assertEqual(mod_inverse(5, 26), 21)

    # Defining the test_encrypt_msg method to test the encrypt_msg function
    def test_encrypt_msg(self):
        # Defining the public_key value
        public_key = (23707, 29)
        # Defining the message value
        message = "HELLO"
        # Calling the encrypt_msg function and storing the result in the encrypted_msg variable
        encrypted_msg = encrypt_msg(message, public_key)
        # Asserting that the encrypted_msg is equal to the expected value
        self.assertEqual(encrypted_msg, f"丰䱈ՑՑದ")

    # Defining the test_decrypt_msg method to test the decrypt_msg function
    def test_decrypt_msg(self):
        # Defining the first private_key value
        private_key = (151, 157, 8069)
        # Defining the cipher_text value
        cipher_text = "丰䱈ՑՑದ"
        # Calling the decrypt_msg function and storing the result in the message variable
        message = decrypt_msg(cipher_text, private_key)
        # Asserting that the message is equal to the expected value
        self.assertEqual(message, "HELLO")

        # Defining the second private_key value
        private_key = (17, 19, 187)
        # Defining the cipher_text value
        cipher_text = "AFLANSFS2"
        # Calling the decrypt_msg function and storing the result in the message variable
        message = decrypt_msg(cipher_text, private_key)
        # Asserting that the message is equal to the expected value
        self.assertEqual(message, "\x1bĺ\x13\x1bG\x1aĺ\x1a2")

if __name__ == "__main__":
    unittest.main()
