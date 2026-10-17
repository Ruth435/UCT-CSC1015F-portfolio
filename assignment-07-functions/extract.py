# program that calculates the volume of a cylinder given integer values for its diameter and height.
# Ruth-ann Rudolph - RDLRUT001
# 03/04/2023

def location(block):
    """extracts the location - the name of the place - from a block of information"""
    location = ""
    i = len(block)-5
    while block[i-1] != "S":    #loops backwards through the words of the location (they are stored in reverse)
        location = location + block[i] #rebuilds the location, flips it
        i = i- 1
    return location.title()
    
def temperature(block):
    """extracts the temperature from a block of information"""
    start = block.find(" ")
    end = block.find("_")
    temperature = float(block[start:end])
    return temperature


def x_coordinate(block):
    """extracts the x-coordinate from a block of information"""
    start = block.find(":")
    end = block.find(",")
    x_coordinate = block[start+1:end]
    return x_coordinate


def y_coordinate(block):
    """extracts the y-coordinate from a block of information"""
    block = block[6:] #cuts out the first word in the block to allow for easy searching
    start = block.find(",")
    end = block.find("S")
    if end == -1:       #if "S" is not found, checks for "N"
        end = block.find("N")
    y_coordinate = block[start+1:end+1]
    return y_coordinate


def pressure(block):
    """extracts the pressure from a block of information"""
    start = block.find("_")
    end = block.find(":")
    pressure = float(block[start+1:end])
    return pressure

def get_block(data):
    """extracts a block of information in a set format from the input data"""
    begin = data.find("BEGIN")
    end = data.find("END")
    return data[begin:end+3]

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block)) #prints the x and y coordinates
    print('Temperature: {:.2f} C'.format(temperature(block))) #formats and prints the temperature
    print('Pressure: {:.2f} hPa'.format(pressure(block))) #formats and prints the pressure 

if __name__=='__main__':
    main()
