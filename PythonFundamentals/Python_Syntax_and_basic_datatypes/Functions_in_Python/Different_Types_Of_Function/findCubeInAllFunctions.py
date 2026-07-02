# No Arguments and No return value
def cube():
    a = 2
    print(f"The cube of 2 is {a * a * a}")
cube()

# No Arguments but returns value
def cube():
    a = 4
    return (a * a * a)
print(f"The cube of 4 is {cube()}")

# Aruguments with no return value
def cube(a):
    print(f"The cube of {a} is {a * a * a}")
cube(3)

# Arguments with return value
def cube(a):
    return  a * a * a
print(f"The cube of 5 is {cube(5)}")