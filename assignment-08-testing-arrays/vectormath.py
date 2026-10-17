# to do basic vector calculations in 2 dimensions: addition, dot product and cross product.
# Ruth-ann Rudolph RDLRUT001
# 18/04/2023

import math

def vector_magnitude():
    """calculates The magnitude of a vector, from user input and outputs the answer to one decimal place"""
    components = input("Enter the components of the vector separated by spaces:\n")
    Components_Array = components.split() #splits the vector into x and y (possibly z as well)
    if len(Components_Array) == 2:
        magnitude_v = math.sqrt((eval(Components_Array[0])**2)+(eval(Components_Array[1])**2)) #calculates for a 2 dimentional vector
    elif len(Components_Array) == 3:
        magnitude_v = math.sqrt((eval(Components_Array[0])**2)+(eval(Components_Array[1])**2)+(eval(Components_Array[2])**2)) #calculates for a 3 dimentional vector
    magnitude_v = round(magnitude_v,1)
    output = "Magnitude of the vector is: " + str(magnitude_v)
    return output

def vector_add():
    """Given two vectors, and outputs the result of adding them together"""
    components_1 = input("Enter the components of the first vector separated by spaces:\n")
    components_2 = input("Enter the components of the second vector separated by spaces:\n")
    if len(components_1) == len(components_2): #checks that the vectors are both of the same length (2d or 3d)
        Components_Array_1 = components_1.split() #splits the vector into x and y (possibly z as well)
        Components_Array_2 = components_2.split() #splits the vector into x and y (possibly z as well)
        x_sum = eval(Components_Array_1[0]) + eval(Components_Array_2[0])
        y_sum = eval(Components_Array_1[1]) + eval(Components_Array_2[1])
        if len(Components_Array_1) == len(Components_Array_2) and len(Components_Array_1) == 3: # checks if there is a z component
            z_sum = eval(Components_Array_1[2]) + eval(Components_Array_2[2])
            output = "Sum of the vectors is: (" + str(x_sum) + ", " + str(y_sum) + ", " + str(z_sum) + ")"
        else:
            output = "Sum of the vectors is: (" + str(x_sum) + ", " + str(y_sum) + ")"
    else:
        return "Error: Vectors must have the same length."
    return output
    
def Scalar_Multiply():
    """Multiplies the entered vector by a scalar value and outputs the result"""
    components = input("Enter the components of the vector separated by spaces:\n")
    multiply = eval(input("Enter the scalar:\n"))
    Components_Array = components.split() #splits the vector into x and y (possibly z as well)
    x_multiply = eval(Components_Array[0])*multiply
    y_multiply = eval(Components_Array[1])*multiply
    if len(Components_Array)  == 3: # checks if the vecotr is 3 dimentional
        z_multiply = eval(Components_Array[2])*multiply
        output = "Scalar multiplication of the vector is: (" + str(x_multiply) + ", " + str(y_multiply) + ", " + str(z_multiply) + ")"
    else:
        output = "Scalar multiplication of the vector is: (" + str(x_multiply) + ", " + str(y_multiply) + ")"
    return output

def dot_product():
    """Given two vectors 𝑣 = (𝑣𝑥, 𝑣𝑦), and 𝑣′ = (𝑣𝑥′, 𝑣𝑦′), their dot product is the value of (𝑣𝑥 × 𝑣𝑥′ + 𝑣𝑦 × 𝑣𝑦′).
    outputs this value"""
    components_1 = input("Enter the components of the first vector separated by spaces:\n")
    components_2 = input("Enter the components of the second vector separated by spaces:\n")
    if len(components_1) == len(components_2): # checks that the vectors are of the same dimentions (2d or 3d)
        Components_Array_1 = components_1.split() #splits the vector into x and y (possibly z as well)
        Components_Array_2 = components_2.split() #splits the vector into x and y (possibly z as well)
        x_product = eval(Components_Array_1[0]) * eval(Components_Array_2[0])
        y_product = eval(Components_Array_1[1]) * eval(Components_Array_2[1])
        if len(Components_Array_1) == len(Components_Array_2) and len(Components_Array_1) == 3: #checks if it is a 3 dimentinal vector
            z_product = eval(Components_Array_1[2]) * eval(Components_Array_2[2])
            total = x_product + y_product + z_product
        else:
            total = x_product + y_product
        output = "Dot product of the vectors is: " + str(total)
    else:
        return "Error: Vectors must have the same length."
    return output

def cross_product():
    """Given two vectors 𝑣 = (𝑣𝑥, 𝑣𝑦, 𝑣𝑧), 𝑣′ = (𝑣𝑥′, 𝑣𝑦′, 𝑣𝑧′) 
    their cross product is the new vector 𝑣′′ = (𝑣𝑦𝑣𝑧′ − 𝑣𝑧𝑣𝑦′, 𝑣𝑧𝑣𝑥′ −𝑣𝑥𝑣𝑧′, 𝑣𝑥𝑣𝑦′).
    outputs this value"""
    components_1 = input("Enter the components of the first 3-dimensional vector separated by spaces:\n")
    components_2 = input("Enter the components of the second 3-dimensional vector separated by spaces:\n")
    Components_Array_1 = components_1.split() #splits the vector into x, y and z as well
    Components_Array_2 = components_2.split() #splits the vector into x, y and z as well
    if len(Components_Array_1) == len(Components_Array_2) and len(Components_Array_1) == 3: #checks that the input meets the requirements
        product_1 = (eval(Components_Array_1[1]) * eval(Components_Array_2[2])) - (eval(Components_Array_1[2]) * eval(Components_Array_2[1]))
        product_2 = (eval(Components_Array_1[2]) * eval(Components_Array_2[0])) - (eval(Components_Array_1[0]) * eval(Components_Array_2[2]))
        product_3 = (eval(Components_Array_1[0]) * eval(Components_Array_2[1])) - (eval(Components_Array_1[1]) * eval(Components_Array_2[0]))
        total = product_1 + product_2 + product_3
        output = "Cross product of the vectors is: (" + str(product_1) + ", " + str(product_2) + ", " + str(product_3) + ")"
    else:
        return "Error: Vectors must have the same length and 3-dimensional."
    return output
    
    
option = 0 #creats a variable to hold the users input
while option != 6: #until the user chooses the "6. exit" option
    print("Choose an option:\n1. Magnitude of a vector\n2. Vector addition\n3. Scalar multiplication\n4. Dot product of two vectors\n5. Cross product of two 3-dimensional vectors\n6. Exit")
    option = input("")
    if option.isdigit(): #checks that the user did input a number
        option = int(option)   
    if option == 1:
        print(vector_magnitude()) #calls the vector_magnitude function
    elif option == 2:
        print(vector_add()) #calls the vector_add function
    elif option == 3:
        print(Scalar_Multiply()) #calls the Scalar_Multiply function
    elif option == 4:
        print(dot_product()) #calls the dot_product function
    elif option == 5:
        print(cross_product()) #calls the cross_product function
    elif option == 6: 
        print("Exiting...")
        break # exits the loop
    else:
        print("Invalid choice. Please choose a valid option.")