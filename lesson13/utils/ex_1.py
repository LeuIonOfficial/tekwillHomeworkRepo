x = input('Anything: ')

try:
    type_of_x = int(x)
except ValueError:
    print(f"{x} cant be integer")
else:
    print(f"{x} can be an integer")

try:
    type_of_x = float(x)
except ValueError:
    print(f"{x} cant be float")
else: 
    print(f"{x} can be a float")

finally:
    print(f"{x} can be a string")