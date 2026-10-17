# searches a file for anagrams of a given word, printing the results in alphabetical order.
#Ruth-ann Rudolph RDLRUT001
# 12/05/2023

try:
    print("***** Anagram Finder *****")
    file = open("EnglishWords.txt", 'r')
    word = (input("Enter a word: \n")).lower()
    word_origanal = {} #will hold a dictionary of letters in the origanal word
    anagrams = [] # will hold anagrangrams of the origanal word
    current_line = ""
    while current_line != "START\n": # skips over the copywrite notice at the start of the file
        current_line = file.readline() 
    for i in word:  #loops over each letter of the given word and adds them to the dictionary
        if i in word_origanal:
            word_origanal[i] += 1 
        else:
            word_origanal[i] = 1
    for line in file: #loops through the words in the file (after copywrite statement)
        new_word = line
        new_word = new_word.replace("\n", '') #removes the new line characters    
        check_word = {} #creates a dictionary of the letters in the current word in the file
        for i in new_word:
            if i in check_word:
                check_word[i] += 1
            else:
                check_word[i] = 1
        if check_word == word_origanal and not new_word == word: #checks if the word is an anagram of the origanal word
            anagrams.append(new_word)        
    if len(anagrams) > 0: #checks if there are anagrams found
        anagrams.sort()
        print(anagrams)
    else:
        print("Sorry, anagrams of '",word,"' could not be found.", sep = "")
    file.close()
except IOError: #error incase the file was not found
    print("Sorry, could not find file 'EnglishWords.txt'.")