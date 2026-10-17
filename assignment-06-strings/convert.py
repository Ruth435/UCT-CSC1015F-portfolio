# program that accepts a date and time and outputs the same information in the following long form
# Ruth-ann Rudolph
# 17 March 2023

old_date = input("Enter the date and time (yyyy-mm-dd hh:mm):\n") #gets the date from the user
space = old_date.find(" ")                                        #finds the first space in the date entered
year = old_date[2:4]                                              #creates a new variable to contin the last 2 digits of the year
month = int(old_date[5:7])                                        #creates a new variable to contain the month as an integer
day = old_date[8:10]                                              #creates a new variable to contain the day
time = int(old_date[space+1:space+3])                             #creates a new variable to contain the hour of time as an integer
if time > 12:                                                     #checks if time needs to be converted out of 24 hour time
    time = time-12                                                #converts the time back to 12 hour time
    if time < 9:
        new_date = old_date[space+2:] + " pm on the "             #creates a new date with the new format of time for times less than 10
    new_date = str(time) + old_date[space+3:] + " pm on the "     #creates a new date with the new format of time
elif time > 9 and time <12:                                       #checks if time is 2 digits long
    new_date = old_date[space+1:] + " am on the "                 #creates a new date with the new format of time
elif time == 0:
    new_date = "12" + old_date[space+3:] + " am on the "          #creates a new date with the new format of time for midnight
elif time == 12:
    new_date = "12" + old_date[space+3:] + " pm on the "          #creates a new date with the new format of time for mid-day
else:
    new_date = old_date[space+2:] + " am on the "                 #creates a new date with the new format of time for times less than 10

if int(day[1:]) == 1 and int(day) != 11:                                             #Checks if the last digit of the day is 1 to add st to the date
    new_date = new_date + str(int(day)) +"st of"                  #adds st to the date format
elif int(day[1:]) == 2:                                           #Checks if the last digit of the day is 2 to add nd to the date
    new_date = new_date + str(int(day)) +"nd of"                  #adds nd to the date format
elif int(day[1:]) == 3:                                           #Checks if the last digit of the day is 3 to add rd to the date
    new_date = new_date + str(int(day)) +"rd of"                  #adds rd to the date format
else:
    new_date = new_date + str(int(day)) + "th of"                 #adds th to the date format

if month == 1:                                                    #this section checks what the month is, from the integer value and adds the corsesponding month (in words) to the new date variable
    new_date = new_date + " January \'" + year
elif month == 2:
    new_date = new_date + " February \'" + year
elif month == 3:
    new_date = new_date + " March \'" + year
elif month == 4:
    new_date = new_date + " April \'" + year
elif month == 5:
    new_date = new_date + " May \'" + year
elif month == 6:
    new_date = new_date + " June \'" + year
elif month == 7:
    new_date = new_date + " July \'" + year
elif month == 8:
    new_date = new_date + " August \'" + year
elif month == 9:
    new_date = new_date + " September \'" + year
elif month == 10:
    new_date = new_date + " October \'" + year
elif month == 11:
    new_date = new_date + " November \'" + year
else:
    new_date = new_date + " December \'" + year
print(new_date)                                   # prints out the new, formatted date