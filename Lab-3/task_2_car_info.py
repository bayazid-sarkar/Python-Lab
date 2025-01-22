def make_car(manufacturer, model_name, fitness_status, **kwargs):
    car_info = {
        'manufacturer': manufacturer,
        'model_name': model_name,
        'fitness_status': fitness_status
    }
    car_info.update(kwargs)
    return car_info

manufacturer = input("Enter car manufacturer: ")
model_name = input("Enter car model name: ")
fitness_status = input("Enter car fitness status (e.g., Fit/Not Fit): ")

print("Add additional features (enter 'done' to finish):")
additional_features = {}
while True:
    key = input("Feature name: ")
    if key.lower() == 'done':
        break
    value = input(f"Value for {key}: ")
    additional_features[key] = value

car = make_car(manufacturer, model_name, fitness_status, **additional_features)

print("Car Information:")
print(car)
