# Base class for all employees
class Employee:
    
    # Initialize employee details
    def __init__(self, empname, empage, empsalary, emprole):
        self.empname = empname
        self.empage = empage
        self.empsalary = empsalary
        self.emprole = emprole
    
    # Show employee information
    def display_info(self):
        print(f"{self.empname}, {self.empage}, {self.empsalary}, {self.emprole}")
    
    # Default behavior of an employee
    def work(self):
        print("Inside parent work")
    
# Child class: Developer inherits Employee
class Developer(Employee):
    
    # Override parent method for developer-specific work
    def work(self):
        print("Development")
        
    # Extra method for developer
    def project(self):
        print("Developing project")

# Child class: Tester inherits Employee
class Tester(Employee):
    # Override parent method for tester-specific work
    def work(self):
        print("Testing")
        pass
    
# Create objects and test inheritance
d = Developer("Sulaim", 21, 56000, "Developer")
d.display_info()
d.work()

t = Tester("Saadath", 20, 70000, "Tester")
t.display_info()
t.work()
    