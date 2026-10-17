# program that calculates the volume of a cylinder given integer values for its diameter and height.
# Ruth-ann Rudolph - RDLRUT001
# 03/04/2023

import math 
def circle_area(diameter): 
    """caluclates the area of the circle from the diameter"""
    area = 1/4*(math.pi)*diameter**2
    return area

def cylinder_volume(diameter, height): 
    """caluclates the volume of a cylinder given the diameter of the circle and the height of the cylinder"""
    area = circle_area(diameter) #calls the circle area function
    volume = area*height
    return volume

def main(): 
    diameter = float(input("Enter diameter:\n"))
    height = float(input("Enter height:\n"))
    volume = cylinder_volume(diameter,height) #calls the cylinder volume function
    print ("The volume of the cylinder is", "{:.2f}".format(volume)) #prints the volume of the cylinder to 2 decimal places
    
if __name__=='__main__': 
    main() 