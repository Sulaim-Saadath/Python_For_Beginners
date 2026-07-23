# Creation of tuple
t = (1, 3, 6, 7, 8)
print(f"{t}")

t1 = ("Gamana", 5.4, 100, 'A')
print(f"{t1}")
print(f"{type(t1)}")

# It is not recomended to store a single value inside a tuple beacause it will behave as a int not as tuple 
# => To store only single value and treated as tuple it should written like this
t2 = (3, )
print(f"{type(t2)}")

# Accessing a single element of a index
# Indexing starts from the 0
print(f"{t1[0]}")

# Acessing using negative values (starts from last element of tuple)
print(f"{t1[-4]}")

# Tuple Slicing
print(f"t[1:4]= {t[1:4]}")
print(f"t[:3]= {t[:3]}")

# Tuples are Immuatable - You cannot the change the values Inside Tuple
t1[0] = "Saadath"
print(f"{t1}")

