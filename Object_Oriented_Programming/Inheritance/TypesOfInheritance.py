# 1. Single Inheritance
# One parent class is inherited by one child class.
class AnimalSingle:
    def sound(self):
        print("Animal makes a sound")

class Dog(AnimalSingle):
    def sound(self):
        print("Dog barks")

print("Single Inheritance")
dog = Dog()
dog.sound()

# 2. Multilevel Inheritance
# A class inherits from another class, which itself inherits from another class.
class AnimalMulti:
    def eat(self):
        print("Animal eats")

class Mammal(AnimalMulti):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

print("\nMultilevel Inheritance")
dog = Dog()
dog.eat()
dog.walk()
dog.bark()

# 3. Multiple Inheritance
# A class inherits from more than one parent class.
class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    pass

print("\nMultiple Inheritance")
duck = Duck()
duck.fly()
duck.swim()

# 4. Hierarchical Inheritance
# Multiple child classes inherit from one parent class.
class AnimalHierarchical:
    def info(self):
        print("This is an animal")

class Cat(AnimalHierarchical):
    def sound(self):
        print("Meow")

class Rabbit(AnimalHierarchical):
    def sound(self):
        print("Squeak")

print("\nHierarchical Inheritance")
cat = Cat()
rabbit = Rabbit()
cat.info()
cat.sound()
rabbit.info()
rabbit.sound()

# 5. Hybrid Inheritance
# A combination of two or more inheritance types.
class A:
    def show(self):
        print("Class A")

class B(A):
    def display_b(self):
        print("Class B")

class C(A):
    def display_c(self):
        print("Class C")

class D(B, C):
    pass

print("\nHybrid Inheritance")
d = D()
d.show()
d.display_b()
d.display_c()
