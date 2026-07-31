# public
class Human:
    def __init__(self, name):
        self.name  = name
        pass
h = Human("Sulaim")
print(h.name)

# protected
class Student:
    def __init__(self, name):
        self._name = name
    def display_name(self):
        print(self._name)
s = Student("Saadath")
s.display_name()

# private
class Employee:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
e = Employee("Avoor")
print(e.get_name())
e.set_name("Sulaim")
print(e.get_name())

# Another way of accessing private variable
# Name Mangling -> _classname__name
print("Name Mangling",e._Employee__name)