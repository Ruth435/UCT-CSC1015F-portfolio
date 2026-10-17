# Program to determine if it is a leap year or not
# Ruth-ann Rudolph
# 24/02/2023

year = int(input("Enter a year:\n"))
if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")