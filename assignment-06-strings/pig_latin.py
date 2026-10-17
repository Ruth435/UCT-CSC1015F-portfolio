# program which accepts a sentence as input and translates it to a variant of Pig Latin
# Ruth-ann Rudolph
# 18 March 2023

sentence = input("Enter a sentence:\n")                 #gets the sentence from the user
sentence = sentence.lower()                             #puts the sentence into lower case
pig_latin = ""                                          #creates an empty variable to which the adjusted words will be added
space = 0

while space != -1:                                      #checks that there is another space in the sentence and loops until there isn't
    space = sentence.find(" ")                          #finds the next space in the sentence
    if sentence[0:1] in "aeiou":                        #checks if the first letter of the word is a vowel
        if space == -1:                                 #checks if the current word is the last word in the sentence
            pig_latin = pig_latin + sentence[0:] + "way" #converts the word to pig latin
        else:                                            #if it is not the last word in the sentence
            pig_latin = pig_latin + sentence[0:space] + "way" #converts the word to pig latin
    else:                                                     #checks if the first letter is a is not a vowel
        consonant = "a"                                       #adds the letter a to a new variable which will store the leading consonants
        while not (sentence[0:1] in "aeiou"):                 #loops until the letter is a vowel
            consonant = consonant + sentence[0:1]             #adds the leading consonants to the variable
            sentence = sentence[1:]                           #adjusts the sentence to exclude the leading consonants
        if space == -1:                                             #checks if the current word is the last word in the sentence
            pig_latin = pig_latin + sentence[0:] + consonant + "ay" #converts the word to pig latin
        else:                                                       #if it is not the last word in the sentence
            space = sentence.find(" ")                              #finds the next space in the sentence
            pig_latin = pig_latin + sentence[0:space] + consonant + "ay" #converts the word to pig latin
    pig_latin = pig_latin + " "                                          #adds a space to the new pig latin sentence
    sentence = sentence[space+1:]                                        #adjusts the sentence to exclude the adjusted word
print(pig_latin)                                                         #prints the converted sentence