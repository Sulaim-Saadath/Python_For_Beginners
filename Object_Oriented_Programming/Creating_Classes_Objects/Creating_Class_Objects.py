class Mentor:
    # Set basic details for the object
    def define_states(self):
        self.name = "Saadath"
        self.age = 21
        self.position = "Java Full Stack Developer"

    # Show a teaching message
    def teach(self):
        print(f"{self.name} is teaching.")

    # Show the mentor's role
    def groom(self):
        self.teach()
        print(f"{self.name} Grooms for the role {self.position}")

# Create an object of Mentor
m = Mentor()

# Give the object some values
m.define_states()

# Access values from the object
name = m.name
age = m.age
role = m.position

# Print the object's details
print(f"{name}, {age}, {role}")

# Call methods using the object
m.teach()
m.groom()