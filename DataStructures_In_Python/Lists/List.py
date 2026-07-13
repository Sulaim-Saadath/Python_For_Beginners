# List - Collection of Multiple values stored in a single variable
# Stores in ordered , stores duplicate values
# Lists are mutable
# List store different values (Heterogenous data)

numbers = [10, 20, 30, 40]
print(f"{numbers}")

data = [10, 3.14, "Sulaim", True]
print(f"{data}")

# Access the elements inside list
# Index starts for 0
print(f"{data[2]}") # Sulaim

# List is mutable
data[2] = "Saadath"
print(f"{data}")

# Inbuilt Methods in List


# 1) Add Elements inside List
# Element is always added at the end of the list
numbers.append(50)
print(f"{numbers}")

# Insert the element at particular Index
numbers.insert(1, 60)
print(f"{numbers}") 

# 2) Remove the Elements
numbers.remove(50)
print(f"{numbers}") 

# To remove element at particular index
numbers.pop(1)
print(f"{numbers}")


# 3) Length of the List
print(f"{len(numbers)}")