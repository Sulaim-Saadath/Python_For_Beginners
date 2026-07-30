print("----------------------Method Overriding (Run-time polymorphism)----------------------")

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks") # Overriding
c = Dog()
c.sound()

print("----------------------Method Overloading (Compile-time polymorphism)----------------------")
class Test:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
t = Test()
# print(t.add(2, 4))
print(t.add(4, 5, 7))

# Method overloading not possible in pythons
# To do it we make use of *args (Flexible Arguments, Functional Arguments)
class Math:
    def add(self, *numbers):
        list1 = numbers
        print(type(list1))
        sum = 0
        for n in numbers:
            sum += n 
        return sum
m = Math()
print(m.add(2,3))
print(m.add(1,2,3,4,5))

# Here * means it takes as many number of paramteres and it is stored inside a tuple

print("----------------------Operator Overloading (Compile-time polymorphism)----------------------")
#  Operator behave differnetly based on the operands

print(5 + 3) # 8
print("Hi" + " All") # Hi All

class Number:
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

class Student:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
s1 = Student(85)
s2 = Student(90)
print(s1 + s2) # 175

print("----------------------Duck Typing----------------------")
class Parrot:
    def fly(self):
        print("Parrot flying in the sky!")
    
class Aeroplane:
    def fly(self):
        print("Airplane is taking off")

# Funtion using duck typing
def make_it_fly(thing):
    thing.fly()

parrot = Parrot()
aeroplane = Aeroplane()
make_it_fly(parrot)
make_it_fly(aeroplane)