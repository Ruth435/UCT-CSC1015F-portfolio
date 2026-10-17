# asks the user to enter a word length and a filename. The program will search the ‘EnglishWords.txt’ file (of question 1) for sets of words that are that length and are anagrams of each other, and will write the results to a file with the given filename.
#Ruth-ann Rudolph RDLRUT001
# 12/05/2023

def check_anargams (origanal_word, word_list, output):  
    """checks for anagrams and outputs the results to a file as well as a list of the outputs to the main function"""
    output_updated = []
    word_dict = {}
    anagrams = []
    anagrams.append(origanal_word) #adds the input word to the anagrams list
    for i in origanal_word: #creates a dictionary of the letters in the origanal word
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    
    for num in word_list: #checks over the words in the list provided
        new_word = num
        check_word = {}
        for i in new_word: #creates a dictionary of the letters of the current word from the list which is being checked
            if i in check_word:
                check_word[i] += 1
            else:
                check_word[i] = 1
        if check_word == word_dict and not new_word == origanal_word and not (check_word in output): #checks if the word is an anagram that has not already been used
            anagrams.append(new_word)
    if len(anagrams) > 1: #checks that there are at least 2 words in the anagram list
        anagrams.sort()
        output_updated = anagrams + output #makes a list of what is being sent to the file
        print(anagrams, file = file_w) #writes the list to the file
    return output_updated #returns the output
    
try:
    print("***** Anagram Set Search *****")
    num_letters = int(input("Enter word length:\n"))
    print("Searching...")
    file_name = input("Enter file name:\n")
    file = open("EnglishWords.txt", 'r')
    print("Writing results...")  
    word_list = []
    current_line = ""
    while current_line != "START\n": #skips over the copywrite statement 
        current_line = file.readline()   
    for line in file: #loops through the remaining lines in the file
        line = line.replace("\n", '') #removes new line statements
        if len(line) == num_letters: #checks if the word contains the right number of letters
            new_word = line.lower()
            if not new_word in word_list: #checks that the word is not a duplicate
                word_list.append(new_word)
    word_list.sort()
    file.close()
    file_w = open(file_name, "w")
    output = []
    for word in word_list: #loops through the list of words with the specified number of letters
        if not word in output : #checks that the word has not already been used
            output = output + (check_anargams(word,word_list, output))
    file_w.close()
except IOError:  #error incase the file was not found
    print("Sorry, could not find file '" ,file_name, "'.", sep = '')