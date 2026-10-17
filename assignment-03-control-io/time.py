# program to determine if the user has entered a valid time
# Ruth-ann Rudolph
# 24/02/2023

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
    print ("Your time is valid.")
else:
    print ("Your time is invalid.")