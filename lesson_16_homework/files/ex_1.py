import os

file = {
    "file_name": input("Input file Name (indicate format): "),
    "file_directory": input("Input file location: ")
}

with open(os.path.join(file["file_directory"], file["file_name"]), "w+") as file:
    pass

file_name = file["file_name"]
file_directory = file["file_directory"]

print(f'File {file["file_name"]} created in {file["file_directory"]}.')
