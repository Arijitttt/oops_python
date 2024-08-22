#Add a method to the Car class that displays the full name of the car (brand and the model).

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Lamb","toyota")
my_new_car = Car("Tata","Safari")

print(my_new_car.full_name())