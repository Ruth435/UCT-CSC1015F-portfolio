# program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a).
# Ruth-ann Rudolph RDLRUT001
# 21/04/2023

def encrypts (i):
    """uses recursion to encrypt a message by converting all the lowercase characters to the next character"""
    if len(i) == 0: # checks if the string is empty
        return ""
    else:
        char = ord(i[0:1]) #gets the characters unicode representation
        if char >= ord("a") and char <= ord("z"): #checks if the character is a lowercase letter 
            if char == ord("z"): 
                char = ord("a") #coverts z to a
            else:
                char = char + 1 #increases the character by 1 (moves it to the next character)
            return chr(char) + encrypts(i[1:]) # returns the character and calls the cunction on the rest of the string
        return i[0:1] + encrypts(i[1:]) #retuns the character (not a lowercase letter) and calls the function on the rest of the string
    
entered = input("Enter a message:\n")
print ("Encrypted message:\n",encrypts(entered),sep ="")