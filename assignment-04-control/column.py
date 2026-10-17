# a program that asks the user to enter a number, n, where -6<n<2. Starting from n, the program will print out every 7th number in the range n to n+41.
# Ruth-ann Rudolph
# 03/03/2023

n = int(input("Enter a number:\n"))
if n > -6 and n < 2:
    for n in range (n,n+41,7):
        if n < 10 and n > -1:           #checks if the number needs a space before it (if it takes a single character to print)
            print ("",n)
        else:
            print (n)        
        