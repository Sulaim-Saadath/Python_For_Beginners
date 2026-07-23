# Length of tuple
tup = (1, 2, 3, 4)
t = (1, 3, 6, 7, 8)
print(f"{len(tup)}")

# Joining two tuples
print(f"{t + tup}")

# Repeat multiple value
t1 = (3, )
print(f"{t1 * 3}")

# Using tuple we can return multiple values
def name():
    n1 = "Avoor"
    n2 = "Sulaim"
    n3 = "Saadath"
    return (n1, n2, n3)

print(f"{name()}")

# Packing and Unpacking of tuple

# Packing
student = ("Ravi", 20, "Male")

# Unpacking
name, age, gender = student
print(f"{name}")
print(f"{age}")
print(f"{gender}")