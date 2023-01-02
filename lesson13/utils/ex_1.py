def check_int(number):
    try:
        return int(x)
    except ValueError:
        return None


def check_float(number):
    try:
        return float(x)
    except ValueError:
        return None

x = input('Anything: ')

print(check_int(x))
    