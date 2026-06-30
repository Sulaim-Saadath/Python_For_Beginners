# Inbuilt String Methods - Single Programs

s = "kodNestTechnologies123"

print(f"Original String: {s}")

# Case Conversion Methods
print(f"upper(): {s.upper()}")
print(f"lower(): {s.lower()}")
print(f"capitalize(): {s.capitalize()}")
print(f"title(): {s.title()}")
print(f"swap(): {s.swapcase()}")

# Searching and counting
print(f"find(\"Nest\"): " ,s.find("Nest"))
print(f"count('0'): ", s.count("e"))

# Replace
newString = s.replace("123", "2025")
print(f"replace('123', '2025'): {newString}")

# Starts and endswith
print(f"startswith('  kod'): {s.startswith('  kod')}")
print(f"endswith('123  '): {s.endswith('123  ')}")

# Split and join

words = s.split(" ")
print(f"{words}")

print(f"{'-'.join(words)}")

# Strip spaces

# strip() - deletes both sides
print(f"{s.strip()}")

# rstrip() - strips only right end spaces
print(f"{s.rstrip()}")

# lstrip() - strips only left end spaces
print(f"{s.lstrip()}")

# Content checking

# isalpha() - checks if string contins only alphabets
print(f"{s.isalpha()}")

# isdigit() - checks if string contains only numbers
print(f"{s.isdigit()}")

# isalnum() - checks if the string contains both digit and alphabets
print(f"{s.isalnum()}")

# Length - Checks the length of the string
print(f"len(s): {len(s)}")
