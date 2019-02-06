import re
import string

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

a = input()
a = re.sub(r'[{}," "]'.format(string.punctuation), '', a)
a = a.lower()

print(is_palindrome(a))