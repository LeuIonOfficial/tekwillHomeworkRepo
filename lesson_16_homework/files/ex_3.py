file_name = input("Write here the name of the file: ")


with open(file_name, 'w+') as file:
    description = input("Write here the description of the file: ")
    file.write(description)
    pass

with open(file_name, 'r') as file:
    data = file.readlines()
    pass

print(data)
