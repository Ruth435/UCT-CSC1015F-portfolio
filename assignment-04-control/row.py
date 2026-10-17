# a program that asks the user to enter a number, n, where -6<n<93. The program will print a sequence of 7 numbers, starting from that value. 
# Ruth-ann Rudolph
# 03/03/2023

n = int(input("Enter the start number:\n"))
if n > -6 and n < 93:                   #checks that the number is in the correct range 
    for i in range(0,7):                
        if n < 10 and n > -1:           #checks if the number needs a space before it (if it takes a single character to print)
            print ("",n, end = " ")
        else:
            print (n, end = " ")
        n = n + 1    