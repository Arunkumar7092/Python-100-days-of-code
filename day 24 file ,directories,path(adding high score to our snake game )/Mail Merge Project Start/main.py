PLACEHOLDER = "[name]"


with open("/home/developer/Desktop/arun-100/python-100-days/day 24 file ,directories,path(adding high score to our snake game )/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("/home/developer/Desktop/arun-100/python-100-days/day 24 file ,directories,path(adding high score to our snake game )/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,strip_name)
        with open(f"/home/developer/Desktop/arun-100/python-100-days/day 24 file ,directories,path(adding high score to our snake game )/Mail Merge Project Start/Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as output:
            output.write(new_letter)            


