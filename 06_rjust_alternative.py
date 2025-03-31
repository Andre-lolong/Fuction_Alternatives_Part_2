# create a function
# choose width to be justified
# add it to the text
# display
def rjust_alternative(text, width):
    text_len = len(text)
    if text_len >= width:
        return text
    
    space_to_add = width - text_len
    return " " * space_to_add + text

text = input("Enter a text: ")
spaces = int(input("Enter how many spaces you want: "))
print(rjust_alternative(text, spaces))