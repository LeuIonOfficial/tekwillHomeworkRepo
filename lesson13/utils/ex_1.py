def check_int(number):
    try:
        return int(number)
    except ValueError:
        return None


def check_float(number):
    try:
        return float(number)
    except ValueError:
        return None

x = input('Anything: ')

while True:
    y = check_float(x)
    y = check_int(x)
    if y is not None:
        print(f'{x} is Float')
    break


    