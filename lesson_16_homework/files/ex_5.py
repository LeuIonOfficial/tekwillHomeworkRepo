import sys


def main(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        max_line = ''
        max_count = 0
        for line in lines:
            count = len(line.split())
            if count > max_count:
                max_count = count
                max_line = line
        print(max_line)



