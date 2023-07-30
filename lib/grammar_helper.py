def grammar_helper(text):
    valid_punctuation = ["!", "?", "."]
    invalid_punctuation = [",", ";", ":"]

    # Check for empty string:
    if text == "":
        raise Exception("No text to check.")
    text = text.strip()     # Remove all whitespaces before checking anything else

    # Check if the text is all uppercase or not
    # Adjust capitalisation
    if text != text.upper():
        text = text.capitalize()
    
    # Check puntuation:
    if text[-1] in valid_punctuation:
        return text
    elif text[-1] in invalid_punctuation:
        return text[:-1] + "."
    else:
        return text + "."
    
