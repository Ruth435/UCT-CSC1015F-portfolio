# Program to reformat references 
# Ruth-ann Rudolph
# 17 March 2023

original = input("Enter the reference:\n") 
b = original.find("(")                      #finds the begining of the year in the reference
new_reference = original[0:b].title()       #puts the reference in title case up to the date, and stores it in a new variable
original = original[b:]                     #cuts off the editied part of the string to ease fining the correct place in the string
n = original.find(",")                      #finds the first comma in the reamining string
new_reference = new_reference + original[0:7] + original[7:8].upper() + original[8:n].lower() + original[n:] #formats the remaining string and adds it to the new reference
print ("Reformatted reference:\n" + new_reference)  #prints formatted string