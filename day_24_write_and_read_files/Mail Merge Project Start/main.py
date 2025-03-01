PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as invited_names_file:
    names = invited_names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    letter_contents = starting_letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
