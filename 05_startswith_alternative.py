# create a function
# check if it starts with the given prefix
# return true if yes and false if not
def startswith_alternative(text, prefix):
    if len(prefix) > len(text):
        return False
    return text[:len(prefix)] == prefix

main_text = input("Enter something: ")
its_prefix = input("Enter a prefix: ")

print(startswith_alternative(main_text, its_prefix))