# A program to determine if a given number is a perfect number or not (a positive integer that is equal to the sum of its proper divisors)
# Ruth-ann Rudolph 
# 03/03/2023

store_divisors = ""                     #A string to store all the proper divisors
sum = 0                                 # integer to store the sum of the proper divisors
number = int(input("Enter a number:\n"))
divide = 0                              #Stores the number by which the users input will be divided
while divide < number:                  #checks if there is a remainder
    divide = divide + 1
    mod = number%divide                 #checks if divide is a proper divisor of number
    if mod == 0 and number != divide:   #checks that the divisor is not the number its self and that it is a proper divisor
        sum = sum + divide              #Adds divisor to the sum
        store_divisors = store_divisors + str(divide) + " " #Adds the new proper divisor to the string
print ("The proper divisors of", number, "are:")
print (store_divisors, "\n")
if number == sum:                       #checks if the number is eaqual to the sum of its proper divisors
    print (number, "is a perfect number.")
else:
    print (number, "is not a perfect number.")    