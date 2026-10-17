# program that accepts input of 3 lengths of the triangle sides and gives the area
# Ruth-ann Rudolph
# 24/04/2023

from math import sqrt
a = float( input("Enter the length of the first side: "))
b = float( input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))
s = (a + b+ c)/2
Area = s*(s-a)*(s-b)*(s-c)
if Area>0:
    print ("The area of the triangle with sides of length ", a, " and ", b, " and ", c, " is ", round(sqrt(Area),2) , ".", sep = "")
else: 
    print ("Error: The input does not describe a triangle.")