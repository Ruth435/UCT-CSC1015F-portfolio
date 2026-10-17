#  Given the name of a Python program as input, ‘tracer.py’ will insert a trace statement at the beginning of each function definition. Given the name of a program that already contains trace statements, ‘tracer.py’ will remove them.
#Ruth-ann Rudolph RDLRUT001
# 12/05/2023
def remove (file):
   """removes trace statements from the program file"""
   print("Program contains trace statements\nRemoving...",end="")
   new_file = [] #array to hold the data that will overwrite the origanal file
   for num in range (len(file)): #loops ove the whole file
      current_line = file[num]
      find = current_line.find("DEBUG") #lools for the trace statements
      if find == -1:
         new_file.append(current_line) #adds line that does not inclued trace statements to the new file document
   file_fix = open(file_name, 'w')
   for line in new_file:
      print(line, file = file_fix) #adds each line from the old file to the overwriten file
   file_fix.close()

def insert (file):
   """inserts trace statemnts to a program file"""
   print("Inserting...",end="")
   file.insert(0,"\"\"\"DEBUG\"\"\"")
   for num in range (len(file)): #loops through the whole file
      current_line = file[num] 
      if not current_line.find("def") == -1: # finds the functions
         start = current_line.find("def")+4
         end = current_line.find("(")
         function = current_line[start:end] #gets the name of the function 
         add_line = "    \"\"\"DEBUG\"\"\";print(\'" + function + "\')" #adds trace statement to the function
         file.insert(num+1,add_line) # inserts the trace statement to the new file document
   file_fix = open(file_name, 'w')
   for line in file:
      print(line, file = file_fix) #adds each line from the old file to the overwriten file
   file_fix.close()

try:
   print ("***** Program Trace Utility *****")
   file_name = input("Enter the name of the program file: ")
   file = open(file_name, 'r')
   stored_file = file.readlines() #gets the whole contense of the file as a list
   for line in range (len(stored_file)):
      stored_file[line] = stored_file[line].replace("\n", '') #removes the new line characters to prevent double lines when overwriting the file
   file.close()
   found = False #variable to help check for trace statements
   for num in range (len(stored_file)):
      current_line = stored_file[num]
      find = current_line.find("DEBUG")
      if not find == -1: # if trace statements are found in the file
         found = True
   if found == True:
      remove(stored_file) #calls function to remove trace statements if necicary 
   else:
      insert(stored_file) #calls function to add trace statemnts if necicary
except IOError:
   print("Sorry, could not find file '",file_name,"'.",sep="")
finally:
   print("Done")