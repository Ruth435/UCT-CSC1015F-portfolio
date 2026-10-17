#program that calculates the volume of a cylinder given integer values for its diameter and height.
# Ruth-ann Rudolph - RDLRUT001
# 03/04/2023

import math


def day_of_week(day, month, year):
    """calculates the day of the week a particular day falls on from the day, month and year"""
    if month < 12 and month >= 3:   # if statement changes month numbers to be appropriate for the formula 
        month = month - 2
    elif month == 12:
        month = 10
    elif month < 3:
        month = month + 10
    century = int(str(year)[0:2])   #isolates the century from the full year
    year = int(str(year)[2:])       #isolates the last 2 digits from the full year
    week_day = (day + math.floor(2.6*month - 0.2) - 2*century + year + math.floor(year/4) + math.floor(century/4))%7 #formula to calculate the day of the week
    if week_day == 0:   #changes the day to 7 if it is sunday (formula outputs 0)
        week_day = 7
    return week_day

def is_leap(year):
    """checks if the year is a leap year"""
    if year%4 == 0:      #checks if the year is deviable by 4 with no remainder 
        if year%100 == 0 and year%400 != 0: #checks for the exception
            return False
        else:
            return True
    else:
        return False


def month_num(month_name):
    """converts the name of the month to the corresponding number"""
    month_name = month_name.lower()
    if month_name == "january":
        return 1
    elif month_name == "february":
        return 2
    elif month_name == "march":
        return 3
    elif month_name == "april":
        return 4
    elif month_name == "may":
        return 5
    elif month_name == "june":
        return 6
    elif month_name == "july":
        return 7
    elif month_name == "august":
        return 8
    elif month_name == "september":
        return 9
    elif month_name == "october":
        return 10
    elif month_name == "november":
        return 11
    elif month_name == "december":
        return 12

def num_days_in(month_num, year):
    """checks how many days there are in a particular month"""
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
        return 31 
    elif month_num == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    elif month_num == 4 or month_num == 6 or month_num == 9 or 11: 
        return 30   


def num_weeks(month_num, year):
    """checks how many weeks are in a particular month"""
    days = num_days_in(month_num, year)
    days = math.ceil(days/7)
    return days


def week(week_num, start_day, days_in_month):
    """creates a formatted week for the calendar"""
    week = ""
    if week_num == 1:
        for i in range (1,9-start_day):             #loops over each day of the week
            week = week + "{0:>2}".format(i) + " "  #formats the individual days (left alligned)
        return "{0:>21}".format(week)               #formats the first week of the month to the right
    else:
        start = (7*(week_num-1)) - start_day + 2    #calculates the day of the week on which to begin
        for i in range (start, start + 7):          #loops over each day of the week
            week = week + "{0:>2}".format(i) + " "  #formats the individual days (left alligned)
            if i == days_in_month:
                break                               #Stops the loop if the days in the month have all been added
        return week
    
def main():
    month_name = input("Enter month:\n")
    year = input("Enter year:\n")
    print (month_name.title(),"\nMo Tu We Th Fr Sa Su") #prints the layout of the calendar (days of the week)
    month_number = month_num(month_name)
    num_week = num_weeks(month_number,year)
    days_in_month = num_days_in(month_number, year)
    start_day = day_of_week(1, month_number, year)
    for num_week in range(1,num_week + 1):              #loops over the number of weeks in the month
        print(week(num_week,start_day,days_in_month))
    
if __name__=='__main__':
    main() 