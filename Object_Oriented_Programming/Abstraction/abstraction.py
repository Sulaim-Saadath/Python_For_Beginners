from abc import ABC, abstractmethod
class Payement(ABC): # Abstract Class
    @abstractmethod 
    def pay(self): # Abstract Method
        pass
    def payementrecive(self): # Concrete Method
        print("Payement recieved")
class PaymentMethod(Payement):
    def pay(self):
        print("Pay in cash")
paymentMethod = PaymentMethod()
paymentMethod.pay()
paymentMethod.payementrecive()

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starting...")
    def stop(self):
        print("Car is stopping...")
car = Car()
car.start()
car.stop()