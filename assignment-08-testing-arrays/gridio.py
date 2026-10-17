# allows a user to input integer values and query a 2-dimensional array of size 9 X 9 and then ask the user for a pair of coordinates, (x, y), separated by a space and return the value at the position specified by the given coordinates.
# Ruth-ann Rudolph RDLRUT001
# 17/04/2023

string_array = print("Enter an array:")
Array_outer = []
for i in range(0,9): #loops over the rows
    Array_inner = [] #empties the inner array
    string = input("") 
    for p in range (0,9): #loops through each item in the row
        Array_inner.append(string[p:p+1]) #adds the item to the inner array
    Array_outer.append(Array_inner) #adds the inner array to the outer array

coordinates = input("Enter coordinates:\n")
x = int(coordinates[0:1])
y = int(coordinates[2:3])
while x != -1 and y != -1: #until a -1 value is entered for coordinates 
    print("Value = " + str(Array_outer[x][y])) #prints the value at the coordinates entered
    coordinates = input("Enter coordinates:\n")
    if coordinates.find("-1") != -1: #if a -1 is found in the coordinates entered
        x = -1
        y = -1
    else:
        x = int(coordinates[0:1])
        y = int(coordinates[2:3])
print("DONE")