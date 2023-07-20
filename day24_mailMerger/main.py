#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
PLACEHOLDER = '[name]'
with open("Input/Names/invited_names.txt") as nameList:
    names = nameList.readlines()


# reading letter
    with open("Input/Letters/starting_letter.txt") as l:
        letter = l.read()
        for n in names:
            final_name = n.strip()
            new_letter = letter.replace(PLACEHOLDER, final_name)
            print(new_letter)
            with open(f"./Output/ReadyToSend/letter_for_{final_name}.txt", mode="w") as final_invite:
                final_invite.write(new_letter)


