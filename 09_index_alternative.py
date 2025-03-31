# create a function
# check the given input
# if the target input  was there then count the coordinatee
# if the target was not there then return -1
def index_alternative(text, target):
    for i in range(len(text) - len(target) + 1):
        if text[i:i + len(target)] == target:
            return i
    return -1