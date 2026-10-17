# program which accepts a number, n, where -6<n<2 and prints out the numbers n to n+41 as 6 rows of 7 numbers
# Ruth-ann Rudolph
# 11/03/2023

n = int(input("Enter a number between -6 and 2:\n"))    # gets the start number from the user
if n > -6 and n < 2:                                    # checks that the number is in the correct range
    for x in range (6):                                 # loops 6 times to create 6 rows
        for n in range(n,n+7):                          # loops 7 times to create 7 columns, increasing n by one each time it runs
            if n < 10 and n > -1:                       #checks if the number needs a space before it (if it takes a single character to print)
                print ("",n, end = " ")                 # prints n with a leading space
            else:
                print (n, end = " ")                    # prints n without a leading space
        print("")
        n = n +1                                        # increases n by one because this will not be done by the loop, prevents repeated numbers
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")