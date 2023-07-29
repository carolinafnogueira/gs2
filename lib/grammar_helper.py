def grammar_helper(text_string):
    transformed_string = text_string.capitalize()
    end_punctuation_options = ".!"

    if transformed_string[-1] in end_punctuation_options:
        return transformed_string
    else: 
        return transformed_string + "."

# print(grammar_helper("this is an example to work on"))

