# program that prints the calendar for that month in a 6 row by 7 column grid based on user input
# Ruth-ann Rudolph
# 11/02/2023

month = input("Enter the name of a month (e.g. January, ..., December):\n") # gets the month from the user
start_day = int(input("Enter the start day (1 for Monday, ..., 7 for Sunday):\n")) # gets the start day from the user (the day on which the 1st is)
month_end = 0       #creates a variable to hold the number of days in a given month 
valid_month = False #creates a variable which will indicate if the user has entered a real month
valid_day = False   #creates a variable which will indicate if the user has entered a valid start day (1 to 7)
if start_day > 0 and start_day < 8: #checks if the start day is valid
    valid_day = True                #indicates that the start day is valid
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December": #checks if the month has 31 days
        month_end = 31 #indicates the number of days in the month provided it is in the list above
        valid_month = True     #indicates that the month entered is valid
    elif month == "February":  #checks if the month has 28 days
        month_end = 28         #indicates the number of days in the month provided it is in the list above
        valid_month = True     #indicates that the month entered is valid
    elif month == "April" or month == "June" or month == "September" or month == "November": #checks if the month has 30 days
        month_end = 30         #indicates the number of days in the month provided it is in the list above
        valid_month = True     #indicates that the month entered is valid
    else:                      #if the month entered is not a real month
        print("Invalid calendar: you have either entered an incorrect month name or start day.") 
else:                          #if the day entered is not a valid start day
    print("Invalid calendar: you have either entered an incorrect month name or start day.")

if valid_month and valid_day:       #checks that all the user input was valid
    print(month, "Mo Tu We Th Fr Sa Su", sep = "\n") # prints the month and days of the week to form the outline for the calender
    if start_day != 1:              #checks that the start day is not one, for formatting
        for x in range (0,(start_day-1)*3): #loops until the space coresponding to the start space
            print(" ",end = "")             #prints spaces to fill the space before the start day 
        for n in range (1, 9-start_day):    #loops through all the days left in the week
            print ("",n, end = " ")         #prints the days of the month from 1 till the end of the week, correctly formatted
        print()                             #moves to a new line
        n = n+1                             #adds 1 to n so that the numbers do not repeat 
    else:
        print("\n 1  2  3  4  5  6  7")       #prints the days starting from the first day of the week if the start day is 1
        n = 8
    for x in range (5):                     # loops 5 times to create 5 rows
        for n in range(n,n+7):              # loops 7 times to create 7 columns, increasing n by one each time it runs
            if n < 10 and n > -1:           #checks if the number needs a space before it (if it takes a single character to print)
                print ("",n, end = " ")     # prints n with a leading space
            else:
                if n>month_end:             #checks that the loop has not exceeded the number of days in the month
                    print ("   ", end = "") #prints spaces to fill the grid 
                elif n%7 == 0 and start_day == 1 and month_end == 28:   #corrects formatting for the month of Febuary
                    print(n, end = "")      # prints n without spacing
                else:            
                    print (n, end = " ")    # prints n without a leading space
        print("")
        n = n +1                            # increases n by one because this will not be done by the loop, prevents repeated numbers
            