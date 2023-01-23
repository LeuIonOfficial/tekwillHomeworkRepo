import json


def list_all_dishes():
    with open('dishes.json') as file:
        data = json.load(file)
        print(data)


def add_dishes():
    with open('dishes.json', 'w+') as file:
        dishes_from_user = input("What do you want to add: ")
        json.dump(dishes_from_user, file)
        pass
    pass


def menu_text():
    return """
    1: to add dishes
    2: to see all dishes
    """


def options_dict():
    opt_dict = {
        1: add_dishes,
        2: list_all_dishes,
    }
    return opt_dict


def menu_tool(menu_text, stop_word, options_dict):
    while True:
        print(menu_text)
        option = input(f'Select option or type {stop_word}:')
        option = option.lower().strip()
        if option == stop_word:
            break
        if not option.isnumeric():
            print('Invalid option')
            continue
        option = int(option)
        try:
            options_dict[option]()  # Calling the function
        except KeyError as ex:
            print('Invalid option', str(ex))


menu_tool(menu_text=menu_text(), stop_word='stop', options_dict=options_dict())
