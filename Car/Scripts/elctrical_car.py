from car import Car
class Battery():
    """Простая модель аккумулятора"""
    def __init__(self, battery = 100):
        self.battery = battery
    
    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print(f"Этот автомобиль имеет батарею мощностью {self.battery} киловат")


class ElectricCar(Car):
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print(f"Этот автомобиль имеет батарею мощностью {self.battery} киловат")

    def description_name(self):
        """Переопределение родительского метода"""
        desc = (f'{self.year}  {self.make}  {self.model} {self.battery}')
        return desc
