class Vehicle:
    
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_nnumber = wheel_number
        
    def go(self):
        return "vrrrrrroom"
    
    def fill_up_tank(self):
        return "filling up!"
    
class Car(Vehicle):
     def go(self):
         return "VRROOOOOOOOOOOOOOOOOOOOOO!!!!!"
        
    pass
