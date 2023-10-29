def grammar_helper(text):
    # Check for empty string:
    if text == "":
        raise Exception("No text to check.")
    text = text.strip()     # Remove all whitespaces before checking anything else

    # Check if the text is all uppercase or not
    # Adjust capitalisation
    if text != text.upper():
        text = text.capitalize()
    # Check punctuation:
        if text[-1] in "!?.":
            return text
        elif text[-1] in ",:;":
            return text[:-1] + "."
        else:
            return text + "."
    
    
