from average_words import average_words
from number_of_words import num_of_words
from palindrome import palindrome
from reverse_digits import reverse_digits
from reverse_number import reverse_number
from reverse_string import reverse_string

# Average words
words = input("Get the average of a word: ")
print(average_words(words))

# Reverse string
word = input("Reverse this string: ")

# Palindrome
text = input("Test a palindrome: ")
print(palindrome(text))

# Reverse digits
dig = int(input("Insert a digit to see the inversed: "))
print(reverse_digits(dig))
