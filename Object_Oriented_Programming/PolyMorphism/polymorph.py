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
        sum = 0
        for n in numbers:
            sum += n 
        return sum
m = Math()
print(m.add(2,3))
print(m.add(1,2,3,4,5))