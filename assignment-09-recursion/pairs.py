# program that uses a recursive function to count the number of pairs of consecutive characters in a string
# Ruth-ann Rudolph RDLRUT001
# 21/04/2023

def count_pairs (input_):
    """recursive function which  counts the number of pairs of consecutive characters in the input"""
    if len(input_) < 2: #checks if there are less than 2 letters in the input
        return 0
    else: 
        if input_[0] == input_[1]: # checks if the letters in the first and second position are the same
            return 1 + count_pairs(input_[2:]) # adds one to the count and calls the function on the rest of the input (after the pair)
        else:
            return count_pairs(input_[1:]) #Calls the function on the remaining word from the second position 
        
entered = input("Enter a message:\n") 
print ("Number of pairs:" , count_pairs(entered))