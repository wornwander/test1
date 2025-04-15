class vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Бориса: {self.brand}, год выпуска: {self.year}")

class car(vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"автомобиль - Бориса: {self.brand}, год выпуска: {self.year}, количество дверей: {self.number_of_doors}")

class motorcycle(vehicle):
    def __init__(self, brand, year, type_of_handlebar):
        super().__init__(brand, year)
        self.type_of_handlebar = type_of_handlebar

    def display_info(self):
        print(f"мотоцикл - Бориса: {self.brand}, год выпуска: {self.year}, тип руля: {self.type_of_handlebar}")

car_instance = car("lada", 2020, 4)
motorcycle_instance = motorcycle("yamaha", 2018, "спортивный")

car_instance.display_info()
motorcycle_instance.display_info()