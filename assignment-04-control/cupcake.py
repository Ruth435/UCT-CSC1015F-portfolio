# Program to determine whether or not you should eat the food that fell on the floor
# Ruth-ann Rudolph
# 03/03/2023

Decision = ""
print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------") #prints a line of underscores as a seporation tool
print ("Answer the following questions by selecting from among the options.")
seen = input ("Did anyone see you? (yes/no)\n")
if seen == 'yes':
    important_person = input("Was it a boss/lover/parent? (yes/no)\n") 
    if important_person == 'yes':
        expensive = input ("Was it expensive? (yes/no)\n")
        if expensive == 'yes':
            cut_it = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut_it == 'yes':
                Decision = "Eat it."
            else:
                Decision = "Your call."
        else:
            chocolate = input ("Is it chocolate? (yes/no)\n")
            if chocolate == 'yes':
                Decision = "Eat it."
            else:
                Decision = "Don't eat it."
    else:
        Decision = "Eat it."    
else:
    sticky = input ("Was it sticky? (yes/no)\n")
    if sticky == 'yes':
        raw_steak = input("Is it a raw steak? (yes/no)\n")
        if raw_steak == 'yes':
            puma = input ("Are you a puma? (yes/no)\n")
            if puma == 'yes':
                Decision = "Eat it."
            else:
                Decision = "Don't eat it."
        else:
            cat_interference = input("Did the cat lick it? (yes/no)\n")
            if cat_interference == 'yes':
                healthy_cat = input ("Is your cat healthy? (yes/no)\n")
                if healthy_cat == 'yes':
                    Decision = "Eat it."
                else:
                    Decision = "Your call."
            else:
                Decision = "Eat it."
    else:
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus == 'yes':
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus == 'yes':
                Decision = "Eat it."
            else:  
                Decision = "Don't eat it."
        else:
            cat_interference = input("Did the cat lick it? (yes/no)\n")
            if cat_interference == 'yes':
                healthy_cat = input ("Is your cat healthy? (yes/no)\n")
                if healthy_cat == 'yes':
                    Decision = "Eat it."
                else:
                    Decision = "Your call."
            else:
                Decision = "Eat it."
        
print ("Decision:", Decision) # gives the user a decision about if they should or should not eat the food