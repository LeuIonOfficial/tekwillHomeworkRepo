
def plane_ride_cost(city: str):
    try:
        return list_of_destination[city]
    except KeyError:
        print("Destination not found")

def add_new_destination(city: str, price: int):
    list_of_destination[city] = price
    print(list_of_destination.items())

list_of_destination = {
    "Pittsburgh": 222, 
    "Los Angeles": 475,
    "Ohio": 183,
    "Chisinau": 300 
}

while True:
    a = int(input("1, 2, 3 or 4: "))
    if a == 1:
        city = input("Type your destination: ")
        print(plane_ride_cost(city))
    elif a == 2:
        city = str(input("City: "))
        price = int(input("price: "))
        print(add_new_destination(city, price))
    elif a == 3:
        print(list_of_destination)
        city = str(input("Current city: "))
        price = int(input("New price: "))
        print(add_new_destination(city, price))
    else:
        break

    

