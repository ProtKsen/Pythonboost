def normalize(input_string):
    if input_string.isupper():
        if not input_string[-1].isalnum():  # for cases like "CAPS LOCK." delete last symbol
            input_string = input_string[:-1]
        input_string += '!'
    return input_string.capitalize()


assert (normalize("CAPS LOCK DAY IS OVER") == "Caps lock day is over!")
assert (normalize("Today is not caps lock day.") == "Today is not caps lock day.")
assert (normalize("Let us stay calm, no need to panic.") == "Let us stay calm, no need to panic.")