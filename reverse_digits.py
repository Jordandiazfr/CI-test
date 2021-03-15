def reverse_digits(dig):
    if type(dig) == type(0):
        return int(str(dig)[::-1])
    else:
        return str(dig) + " is not a digit"
