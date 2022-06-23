import pickle
from autobus_class import Autobus

def create_autopark():
    n = int(input('Enter the number of buses: '))
    buses = []
    print('--------------------')
    for i in range(1, n+1):
        number = int(input(f'Enter the route number of {i} bus: '))
        start = input(f'Enter the starting point of {i} bus: ')
        destination = input(f'Enter the destination point of {i} bus: ')
        time = input(f'Enter the travel time of {i} bus: ')
        print('--------------------')
        buses.append(Autobus(number, start, destination, time))
    with open('autopark.bin', 'wb') as file:
        pickle.dump(buses, file)

def show_autopark():
    global buses_list
    with open('autopark.bin', 'rb') as file:
        buses_list = pickle.load(file)
    print('ALL BUSES')
    for obj in buses_list:
        obj.info()

def sort_by_number():
    buses_list.sort(key=lambda x: x.number, reverse=True)
    print('ALL BUSES SORTED BY NUMBER')
    for obj in buses_list:
        obj.info()

def search_by_point(city):
    print(f'BUSES WITH CITY {city}')
    for obj in buses_list:
        if obj.start == city or obj.end == city:
            obj.info()

create_autopark()
show_autopark()
sort_by_number()
search_by_point('Prague')