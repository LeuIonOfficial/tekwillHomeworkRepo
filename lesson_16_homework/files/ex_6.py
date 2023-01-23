import json


def open_json():
    with open("employee_list.json") as json_file:
        return json.load(json_file)


def list_name():
    data = open_json()
    for employee in data:
        print(employee['name'])


def list_positions():
    data = open_json()
    positions_list = []
    for position in data:
        positions_list.append(position["position"])
    positions_list = set(positions_list)
    return positions_list



print(list_positions())
