class Car:
    def __init__(self,colour):
        self.colour = colour

    def show(self):
        print(self.colour)
cars = [
    Car('red'),
    Car('blue'),
    Car('green'),
    Car('black')
]

for index,car in enumerate(cars):
    print(cars[car].show())
