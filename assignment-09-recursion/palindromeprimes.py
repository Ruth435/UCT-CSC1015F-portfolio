# program that uses recursive functions to find all palindromic primes between two integers N, M, supplied as input. (
# Ruth-ann Rudolph RDLRUT001
# 21/04/2023

import math
import sys
sys.setrecursionlimit (30000) #increases the number of recursions allowed


def palindromeprimes(start,end):
    """chekcs for all the prime numbers that are palindromes within the given range"""
    num_checked = start
    if num_checked > end: #checks if the number is out of the range
        return ""
    else:
        if isprime(num_checked,math.sqrt(num_checked)): #checks if the number is a prime by calling a function
            if ispalindrome( num_checked): # checks if the number is a palindrome by calling a function
                return str(num_checked) + "\n" + palindromeprimes(num_checked+1,end) #returns the number if it is a palindrome and a prime and calls the function to check the next number in the range
            else:
                return palindromeprimes(num_checked+1,end) #calls the function on the next number in the range     
        else:
            return palindromeprimes(num_checked+1,end)  #calls the function on the next number in the range  
    
    
def isprime(num,check):
    """checks if a number is a prime by recursivly checking if the number is diviable by another (should begin at the square root"""
    check = int(check) #converts the number to be checked to an integer (cuts off any decimal places)
    if check == 1:
        return True #returns true because all numbers are divasable by 1 and this means all other higher numbers have been checked
    else:
        if num%check == 0: #checks if the number is divisable by the "check" variable with no remainder
            return False 
        else:
            return isprime(num,check-1) #checks against the next number
        
def ispalindrome(palindrome):
    """checks if the number is a palindrome through recursion"""
    palindrome_test = str(palindrome) #converts number input to a string
    if not palindrome_test: #checks for an empty string
        return True
    if len(palindrome_test) == 1: #checks if there is only one character in the string
        return True
    if palindrome_test[0] != palindrome_test[len(palindrome_test)-1]: #if the first and last characters do not match
            return False
    else:
        return ispalindrome(palindrome_test[1:len(palindrome_test)-1]) #calls the function on the string excluding the first and last characters

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:\n", palindromeprimes(start,end), sep="")