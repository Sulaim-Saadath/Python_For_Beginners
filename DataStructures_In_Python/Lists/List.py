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

# Traversing inside List
for num in numbers:
    print(num)
    pass


# 4) extend() - Inserting multiple elements inside list
list1 = [1, 2, 3] 
list2 = [4, 5, 6]
list1.extend(list2)
print(f"{list1}")

# 5) sort() - Arranges the element in ascending order
list3 = [4, 1, 3, 2]
list3.sort()
print(f"{list3}")
# To arrange in descnding just reverse after sorting in ascending order
list3.reverse()
print(f"{list3}")

# Taking input inside a list
integers = (input().split())
i = 0
list4 = []
for n in integers:
    list4.append(int(n))
# print(f"{integers}")
print(f"{list4}")

# Merging Two Lists
newList = list1 + list2
print(f"{newList}")