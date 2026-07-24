# Word -> Meaning
# Key -> Value

# Key Features 
# Stores data in key value pairs, ordered (3.7+)
# Mutable (Changable)
# Keys must be unique
# Keys must be immutable (String, number, tuple)

student = {
    "name":"Saadath",
    "age":21,
    "course":"B-tech"
}

# Accessing values
print(student["name"])
print(student.get("age"))
print(student.get("weight", "N/A"))

# Adding / Updating values
student["age"] = 18
student["city"] = "Delhi"
student.update({"city": "Tirupati"})

# Remove Elements
student.pop("age")
del student["course"]
student.popitem() # Removes the last item
# student.clear() # => Clears all the key - value pairs

# Looping through Dictionary
for key in student:
    print(key, student[key])
    pass

for key, value in student.items():
    print(key, value)
    pass

# UseFul Methods
student.keys() # -> returns keys
student.values() # -> returns values
student.items() # -> returns both key and value

marks = {
    "Math":90,
    "Science":85,
    "English":88
}

total = 0
for subject, score in marks.items:
    total += score
    pass
print(f"Total Marks: {total}")
print(f"Average Marks: {total / marks.__len__()}")

# copy() -> copies the key - value pairs of one dictionary to another
d1 = student.copy()
print(d1)

