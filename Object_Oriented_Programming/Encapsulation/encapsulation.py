class Bank:
    def __init__(self, name, balance, code):
        self.name = name
        self.__balance = balance # private
        self._code = code # protected
        pass
    def printBalance(self):
        print(f"{self.name}, {self.__balance}")
        pass
    
    # Setter method
    def set_balance(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.__balance = amount
        pass
    # Getter method
    def get_balance(self):
        return self.__balance
    pass

b = Bank("SBI", 10000, "Er56")
b.printBalance()
# print(b.__balance)  => Cannot be accessed directly
print(b._code)

# To access the private variables we use setters and getters method
print(f"{b.get_balance()}")
b.set_balance(2000)
print(f"{b.get_balance()}")