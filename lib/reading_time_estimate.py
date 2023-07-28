def reading_time_estimate(text_size):
    time_in_min = round(text_size / 200)
    if time_in_min == 0:
        return "No text to be read here"
    else:
        return f"This text will take {time_in_min} minutes to read"