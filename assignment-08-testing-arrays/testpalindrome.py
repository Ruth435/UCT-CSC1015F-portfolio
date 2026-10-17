# path testing for the function which checks if an input is a palindrome
# Ruth-ann Rudolph RDLRUT001
# 17/04/2023

# testchecker.py
"""
>>> import palindrome
>>> palindrome.is_palindrome("a")
True
>>> palindrome.is_palindrome("abba")
True
>>> palindrome.is_palindrome("")
True
>>> palindrome.is_palindrome("aa")
True
>>> palindrome.is_palindrome("abcd")
False

"""
import doctest
doctest.testmod(verbose=True)