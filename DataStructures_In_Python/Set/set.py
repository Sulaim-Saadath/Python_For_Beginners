st = {1, 2, 3, 4}
print(f"{st}")

st1 = set([3,7,1,4])
print(f"{st1}")

# Add element inside set
st.add(8)
print(st)

# Remove (If element not present it gives the error)
st.remove(1)
# Discard (If element not present it will not throw any error)
st.discard(10)

# Memborship
print(3 in st)

# Set Operations
a = {10, 20, 30}
b = {20, 30, 40}

# Union - Combine sets
print(a.union(b))

# Intersect - Common  values
print(a.intersection(b))

# Difference
print(a - b)
print(b - a)

a.issubset(b)

# print(a | b) (Union)
# print(a & b) (Intersection)
# print(a - b) (difference)

# Looping through set
for item in st:
    print(item)
    
# To find whether a set is subset if another set
print(a.issubset(b))
print(a.isdisjoint(b))

sentence = "This is a test. This test is simple."
sentence = sentence.replace(".", "")
print(sentence)