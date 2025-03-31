# create a function
# identify the letters
# if uppercase then return false and true if lowercase
def islower_alternative(text):
    for letters in text:
        if "A" <= letters <= "Z":
            return False
    return True

main_text = input("Enter something: ")
print(islower_alternative(main_text))