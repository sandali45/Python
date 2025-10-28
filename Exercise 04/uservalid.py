


print("The name Should be less than 12 characters, should not contain spaces, digits or all special characters.")

name = input("Enter your name: ")
character_count = len(name)
space_count = name.count(" ")
digi_count =name.isdigit()


if character_count >= 12 or space_count > 0 or digi_count:
    print("Invalid name")
else:
    print("Valid name")