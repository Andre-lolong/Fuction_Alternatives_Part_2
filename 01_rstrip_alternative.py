# create a function
# check if the end is a space
# remove the space
# display output
def rstrip_alternative(text):
    i = len(text)
    while i > 0 and text[i - 1] == " ":
        i -= 1
    return text[:i]
    
statement = input("Enter a text with spaces at the end: ")
print(rstrip_alternative(statement))
