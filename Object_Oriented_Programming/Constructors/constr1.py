class Mentor:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Inside the constructor",self)
    
    def teach(self):
        print(f"{self.name} teaches.")
    
    def groom(self):
        print(f"{self.name} grooms.")
        
m1 = Mentor(input("Enter Mentor name: "), int(input("Enter age: ")), input("Enter gender: "))
print(f"{m1.name}, {m1.age}, {m1.gender}")
m1.teach()
m1.groom()