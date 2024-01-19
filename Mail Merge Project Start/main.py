#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.read()
split_names = names.splitlines()
for invites in split_names:
    with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as mail:
        mail_invite = mail.read()
        replace_mail = mail_invite.replace("[name]", f"{invites}")
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{invites}.txt", "w") as mail:
        mail.write(replace_mail)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp