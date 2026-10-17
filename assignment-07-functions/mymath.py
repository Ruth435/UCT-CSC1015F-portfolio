# accepts an integer, s, from the user and calculates the factorial of an integer n in seporate functions
# Ruth-ann Rudolph - RDLRUT001 - adapted from combine.py by hussein suleman
# 04/04/2023

def get_integer(s):
   """gets an integer value from the user, keeps asking till an integer is entered"""
   print ("Enter ",s,":",sep = "")
   n = input ("")
   while not n.isdigit (): #checks if the value entered by the user is an integer
      print ("Enter ",s,":",sep = "")
      n = input ("")
   n = eval (n)
   return n

def calc_factorial (n):
   """calculates the factorial of the integer"""
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial
