def reverse_digits():
    dig = int(input("Insert a digit to see the inversed: "))
    if type(dig) == type(0):
        return str(dig)[::-1]
    else:
        return str(dig) + " is not a digit"
