class Mentor:
    def __init__(self, name, tech, age):
        self.name = name
        self.age = age
        self.tech = tech
        print("Hello")
        pass
    
    def teach(self):
        print(f"{self.name} teaches")
        pass
    def groom(self):
        print(f"{self.name} grooms")

m1 = Mentor("Sharan", "Java Trainer", "32")
print(f"{m1.name}, {m1.age}, {m1.tech}")
m1.teach()
m1.groom()

m2 = Mentor("Gamana", "Web Technologies", "28")
print(f"{m2.name}, {m2.age}, {m2.tech}")
m2.teach()
m2.groom()
