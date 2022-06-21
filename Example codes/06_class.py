class Car:
    # attributes
    def __init__(self, car_model):
        self.color = ''
        self.model = car_model
        self.fuel = 100
    
    # methods
    def drive(self):
        self.fuel = self.fuel - 1
        
    def print_your_model(self):
        print(f'My model is: {self.model}')
        
    def print_your_fuel(self):
        print(f'My fuel is: {self.fuel}')
    
    def refuel(self, amount):
        self.fuel = amount
# -------------------------------
car1 = Car('ford')
car1.print_your_model()
