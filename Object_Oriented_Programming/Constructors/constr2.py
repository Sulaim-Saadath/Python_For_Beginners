class Student:
    institute = "Kodnest" # Class Attributes
    def __init__(self, name, age):
        self.name = name # Instance Valriable
        self.age = age

        pass
    
    def study(self):
        print(f"{self.name} studies.")
        pass

s1 = Student("Abhi", 20)
print(f"{s1.name}, {s1.age}, {Student.institute}")
s1.study()

s2 = Student("Anu", 21)
print(f"{s2.name}, {s2.age}, {Student.institute}")
s2.study()