
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

new_list_of_destination = {}

while True:
    
    print("""
    1 - to check the price, 
    2 - to add new destination, 
    3 - to change the price
    4 - to exit 
    """)

    a = int(input("Make your chose: "))
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
        list_of_destination.update(new_list_of_destination)
        break

    

