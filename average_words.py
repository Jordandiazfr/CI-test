def average_words(text):
    tempcount = 0
    count = 1
    wordcount = 0
    try:
        for character in text:
            if character == " ":
                tempcount += 1
                if tempcount == 1:
                    count += 1
            else:
                tempcount = 0
                try:
                    if character.isalpha():
                        wordcount += 1
                except:
                    wordcount = wordcount + 0
        if text[0] == " " or text.endswith(" "):
            count -= 1
        try:
            result = wordcount/count
            if result == 0:
                result = "No words"
                return result
            else:
                return result
        except ZeroDivisionError:
            error = "No words"
            return error
    except Exception:
        error = "Not a string"
        return error
