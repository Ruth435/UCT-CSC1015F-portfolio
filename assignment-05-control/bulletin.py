# Program to simulate a simple Bulletin Board System
# Ruth-ann Rudolph
# 16/03/2023

file_list = "List of files: 42.txt, 1015.txt" # creates a list of files and can be appened
selection = ""                                  # creates a selection variable so that the while loop will run at least once
message = "no message yet"                      # sets the default message
while selection != "X" and selection != "x":    # creates a loop that will run untill the user exits 
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it") # prints the welcome and menu options
    selection = input("Enter your selection:\n")    # gets input from the user, the choice from the menu
    if selection == "E" or selection == "e":        # Checks if the user selected "enter a message"
        message = input("Enter the message:\n")     # gets the message from the user
    elif selection == "V" or selection == "v":      # Checks if the user selected "view a message"
        print("The message is:",message)            # prints the stored message or the default message
    elif selection == "L" or selection == "l":      # Checks if the user selected "list files"
        print(file_list)                            
    elif selection == "D" or selection == "d":      # Checks if the user selected "Display file"
        find_file = input("Enter the filename:\n")  # gets the file name
        if find_file == "42.txt":                  
            print("The meaning of life is blah blah blah ...") # prints out the content of file 42
        elif find_file == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy") #prints out the content of file 1015
        else:
            print("File not found")
print("Goodbye!")     #prints goodbye when the user exits the program 