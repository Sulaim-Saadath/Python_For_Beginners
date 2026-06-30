#                   Strings in Python

# Declarations in python

# 1) Using Single quotes
s1 = 'Sulaim Saadath'
print(f"Using single quotes: {s1}\n")

# 2) Using Double quotes
s2 = "Sulaim Saadath"
print(f"Using double quotes{s2}\n")

# 3) Using single triple quotes - used to write multi line string
s3 = '''Hello
my name is
SUliam Saadath'''
print(f"Using single triple quotes{s3}\n")

# 4) Using double triple quotes - used to write multi line string
s4 = """Hello 
my name is
sulaim saadath"""
print(f"Using double triple quotes: {s4}\n")

# In python we don't have concat function we use '+' to combine two strings
s1 = "Hello"
s1 = s1 + " world"
print(f"{s1}")

print(id(s1)) 

# For each string different memory location is allocated
s2 = "Sulaim"
s3 = s2 + "Saadath"
print(s2, id(s1))
print(s3, id(s2))

# In this case the content of string is same So, Python follows memeory efficiency since contents are same the same memory location given to same variables
s4 = "Python"
s5 = "python"
print(s4, id(s4))
print(s5, id(s5))
print(s4 is s5)
print(s4 == s5)