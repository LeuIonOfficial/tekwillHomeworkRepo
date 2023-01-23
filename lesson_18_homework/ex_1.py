my_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindroms = list(filter(lambda x: (x == "".join(reversed(x))), my_list))

print(palindroms)


