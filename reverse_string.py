def reverse_string(string):
    if string != "" and string != " " and type(string) != type(1):
        return string[::-1]
    else:
        return "Not an valid string"
