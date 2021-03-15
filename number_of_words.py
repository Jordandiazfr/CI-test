def num_of_words(text):
    if type(text) == int:
        return "Not an valid word"
    return str(len(text.split())) + " words"
