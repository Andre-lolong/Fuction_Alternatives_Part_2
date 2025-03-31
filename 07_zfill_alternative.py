# create a function
# specify the width
# fill the beginning with zeros to satisfy the width
# display
def zfill_alternative(text, width):
    if len(text) >= width:
        return text
    return "0" * (width - len(text)) + text