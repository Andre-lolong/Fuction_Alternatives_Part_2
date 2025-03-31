# create a function
# check for lowercase letters
# get the ASCII number and shift lowercase to uppercase
# add all the uppercase to the result
def upper_alternative(text):
  result = ""
  for letter in text:
    if 'a' <= letter <= 'z':
      uppercase_letter = chr(ord(letter) - 32)
      result += uppercase_letter
    else:
      result += letter
  return result

text = input("Enter something with lowercase: ")
uppercase = upper_alternative(text)
print(uppercase)