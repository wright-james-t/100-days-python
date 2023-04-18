#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Dear [name],
#
# You are invited to my birthday this Saturday.
#
# Hope you can make it!
#
# Angela

# Aang
# Zuko
# Appa
# Katara
# Sokka
# Momo
# Uncle Iroh
# Toph

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    base_letter = file.read()

with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    name = name.strip("\n")
    named_letter = base_letter.replace(f"[name]", name)
    with open(f"Output/ReadyToSend/letter_to_{name}", mode="w") as file:
        file.write(named_letter)