class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def vehicle_info(self):
        print(f"{self.brand} {self.model} {self.year}")
    
class  Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, doors):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def vehicle_info(self):
        super().vehicle_info()
        print(f"{self.fuel_type}, {self.doors}")
    def start_engine(self, start_time):
        print(f"Engine has started at {start_time}")
    def stop_engine(self, end_time):
        print(f"Engine Stopped at {end_time}")

my_car=Car("BMW", "Model 1", "2024", "Petrol", 4);
my_car.vehicle_info()
my_car.start_engine("10 pm")
my_car.stop_engine("12 am")

