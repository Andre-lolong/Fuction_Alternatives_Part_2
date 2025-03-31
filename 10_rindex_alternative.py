# same as index but backwards
# create a function
# check the given input
# if the input was there then count the coordinate backwards
# if the input was not there then return -1 
def rindex_alternative(text, target):
    for i in range(len(text)- 1, -1, -1):
        if text[i:i + len(target)] == target:
            return i
    return -1

statement = input("Enter something: ")
target_input = input("Enter the target input you want to use rindex on: ")
print(rindex_alternative(statement, target_input))