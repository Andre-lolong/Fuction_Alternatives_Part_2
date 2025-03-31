# create a function
# identify the main text and the suffix
# check if the main text ends with the given suffix
# rmeove suffix
# display the output
def removesuffix_alternative(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text

main_text = input("Enter the main text: ")
suffix = input("Enter a suffix: ")
print(removesuffix_alternative(main_text, suffix))
