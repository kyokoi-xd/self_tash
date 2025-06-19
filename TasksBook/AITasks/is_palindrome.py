import string
import re

def is_palindrome(s):
    table = str.maketrans("", "", string.punctuation + string.whitespace)
    s = s.translate(table)
    s = s.lower()
    return s == s[::-1]
    

print(is_palindrome("A man, a plan, a canal, Panama"))


# Alternative example 1

def is_palindrome(s):
    s = ''.join(filter(lambda c: c.isalnum(), s)).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))

# Alternative example 2

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))