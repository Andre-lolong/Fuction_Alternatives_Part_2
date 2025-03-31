# create a function
# check the given statement
# check if the target value is in the statement
# if yes then add one to the count and repeat untill how many is detected
# display
def count_alternative(text, target):
    count = 0
    for i in range(len(text) - len(target) + 1):
        if text[i:i + len(target)] == target:
            count += 1
    return count