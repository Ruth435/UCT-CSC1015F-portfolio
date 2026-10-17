# Program that accepts a sentence as input and that outputs it as a comma-separated list of lowercase words with a full-stop at the end.
# Ruth-ann Rudolph
# 17 March 2023

sentence = input("Enter a sentence:\n")                 #gets the sentence from the user
word_list = "The word list: "                           #variable to hold the word list, which will be updated as the program works through the sentence
space = sentence.find(" ")                              #finds the first space in the sentence
if space != 0 and space != -1:                          #if there is at least one space in the input
    word_list = word_list + sentence[0:space].lower()   #adds the first word to the word list
elif space ==  -1:                                      #checks if there is not another space, finds the end of the sentence
        word_list = word_list + (sentence[:]).lower()   #adds the last word to the word list
    
while space != -1:                                      #loops as long as there is another space in the sentence
    word_list = word_list + ", "                        #adds a comma to separate the words in the list
    sentence = sentence[space+1:]                       #cuts the last word out of the sentence
    space = sentence.find(" ")                          #finds the first space in the new version of the sentence
    if space ==  -1:                                    #checks if there is not another space, finds the end of the sentence
        word_list = word_list + (sentence[:]).lower()   #adds the last word to the word list
    else:                                               #checks if it is not the end of the sentence
        word_list = word_list + (sentence[0:space]).lower() #adds the next word to the word list
        
word_list = word_list + "."                             #adds a full stop to the word list
print (word_list)                                       #prints the word list