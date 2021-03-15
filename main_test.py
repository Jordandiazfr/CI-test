import unittest
from palindrome import palindrome
from reverse_string import reverse_string
from average_words import average_words
from number_of_words import num_of_words
from reverse_digits import reverse_digits


class TestMainMethod(unittest.TestCase):

    def test_palindrome(self):
        self.assertFalse(palindrome("JOJO"))
        self.assertTrue(palindrome("ovo"))

    def test_average_words(self):
        self.assertEqual(average_words("This is my code"), 3.0)
        self.assertEqual(average_words(0), 'Not a string')

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hola"), "aloh")
        self.assertEqual(reverse_string(""), "Not an valid string")
        self.assertEqual(reverse_string(0), "Not an valid string")

    def test_number_of_words(self):
        self.assertEqual(num_of_words("Jojo is the best"), "4 words")
        self.assertEqual(num_of_words(1), "Not an valid word")

    def test_reverse_digits(self):
        my_str = "x"
        self.assertEqual(reverse_digits(503), 305)
        self.assertEqual(reverse_digits(my_str), f"{my_str} is not a digit")


if __name__ == '__main__':
    unittest.main()
