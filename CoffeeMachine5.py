def get_percentage(number, round_digits=""):
    precision = len(str(round_digits))
    #print(precision)
    if precision == 0:
        percentage = round(number * 100)
    else:
        percentage = round(number * 100, precision)
    return str(percentage) + "%"


print(get_percentage(0.01234))
print(get_percentage(0.0123, 0))
print(get_percentage(0.0123, 1))
print(get_percentage(0.0123, 10))
