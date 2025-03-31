# create a function
# identify the main text and the suffix
# check if the main text ends with the given suffix
# rmeove suffix
# display the output
def removesuffix_alternative(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text

