class Student:

    # Class variable 
    institute = "Kodnest"
    def __init__(self, name, age):
        self.name = name # Instance Variables
        self.age = age
        pass
    
    # Instance Method
    def study(self):
        print(f"{self.name} studies.")
    
    # Class Method
    @classmethod
    def institute_change(cls, new_institute):
        cls.institute = new_institute
    # Static method
    @staticmethod
    def student_trip():
        print("Student like to go for a trip")

Student.institute_change("Kodnest Pvt Ltd")

s1 = Student("Abhi", 21)
print(f"{s1.name}, {s1.age}, {s1.institute}")
print(Student.institute)
s1.study()
s2 = Student("Balu", 22)
print(f"{s2.name}, {s2.age}, {s2.institute}")
s2.study()
s2.student_trip()

Student.student_trip()