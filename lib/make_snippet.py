def make_snippet(string):
    if (type(string)== int):
        raise Exception("Please enter a string")
    if string == "":
        return ""   
    
    split_string = string.split()
    first_five_words = split_string[0:5]
    separator = ' '
    new_string = separator.join(first_five_words)
    if len(split_string) > 5:
        return new_string + "..."
    else:
        return new_string

# print(make_snippet("return first five words is next step")) DELETE THIS