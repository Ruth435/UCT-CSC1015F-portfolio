# Program to write a personalised spam message
# Ruth-ann Rudolph
# 24/02/2023

name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
print()
print("Dearest", name, "\nIt is with a heavy heart that I inform you of the death of my father,")
print("General Fayk", last_name, end = "")
print(", your long lost relative from Mapsfostol.")
print("My father left the sum of ", money, "USD for us, your distant cousins.", sep = "")
print ("Unfortunately, we cannot access the money as it is in a bank in ", country, ".", sep = "")
print ("I desperately need your assistance to access this money.")
print ("I will even pay you generously, 30% of the amount - ", money/100*30, "USD,", sep = "")
print ("for your help.  Please get in touch with me at this email address asap.")
print ("Yours sincerely")
print ("Frank", last_name)