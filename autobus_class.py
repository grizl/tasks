class Autobus:
    def __init__(self, number, start, end, time):
        self.number = number
        self.start = start
        self.end = end
        self.time = time

    def get_number(self):
        print(self.number)

    def set_number(self, new_number):
        self.number = new_number

    def get_start(self):
        print(self.start)
    
    def set_starting_point(self, city):
        self.start = city

    def get_destination(self):
        print(self.end)

    def set_destination(self, city):
        self.end = city
    
    def get_time(self):
        print(self.time)

    def set_time(self, new_time):
        self.time = new_time
    
    def info(self):
        print('--------------------')
        print(f'Route number: {self.number}', 
        f'\nStarting point: {self.start}',
        f'\nDestination point: {self.end}',
        f'\nTravel time: {self.time}')
        print('--------------------')

# if __name__ == '__main__':
#     bus = Autobus(422, 'Moscow', 'Minsk', '10:15')
#     bus.info()
#     bus.set_number(244)
#     bus.get_number()
#     bus.set_destination('Saint Petersburg')
#     bus.set_time('9:05')
#     bus.info()
