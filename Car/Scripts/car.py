class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        desc = (f'{self.year}  {self.make}  {self.model}')
        return desc
    
    def read_odometer(self):
        print(f'Пробег этого авто {self.odometer_reading} км')

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Не стоит')

    def increment_odometer(self, km):
        self.odometer_reading += km

