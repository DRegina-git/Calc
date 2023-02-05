def sum_data(num1, num2):
    return num1 + num2

def diff_data(num1, num2):
    return num1 - num2

def mult_data(num1, num2):
    return num1 * num2

def div_data(num1, num2, par="/"):
    if par == "%":
        return round(num1 % num2, 2)
    elif par == "//":
        return num1 // num2
    return num1 / num2

def pow_data(num1, num2 = None):
    if not num2:
        return num1 ** 0.5
    return num1 ** num2