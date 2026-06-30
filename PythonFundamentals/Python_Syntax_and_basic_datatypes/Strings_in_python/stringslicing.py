text = "Kodnest"

print(f"{text[2:2]}")

print(f"Original String {text}")
print(f"-------------------------------------------------")

# POSITIVE INDEXING
print(f"01: {text[0:4]}")
print(f"02: {text[1:5]}")
print(f"03: {text[2:7]}")
print(f"04: {text[3:6]}")
print(f"05: {text[4:7]}")

# NEGTATIVE INDEX SLICING
print(f"06: {text[-4:-1]}") # nes
print(f"07: {text[-7:-3]}") # kodn
print(f"08: {text[-5:-2]}") # dne
print(f"09: {text[-6:-4]}") # od
print(f"10: {text[-3:-1]}") # es

# MIXED POSITIVE AND NEGATIVE INDEXING
print(f"11: {text[1:-1]}")
print(f"12: {text[2:-2]}")
print(f"13: {text[0:-3]}")
print(f"14: {text[-5:6]}")
print(f"15: {text[-4:7]}")

# EDGE CASES
print(f"16: {text[2:2]}")
print(f"17: {text[5:3]}")
print(f"18: {text[10:15]}")
print(f"19: {text[-10:3]}")

'''
# text[-10:3] means:
# Start from index -10 → which is out of range, so Python treats it as index 0 (start of string)
# End at index 3 → but 3 is not included (Python slicing excludes end index)
# So effectively it becomes text[0:3]

# text[0:3] → takes characters from index 0, 1, 2 → "Kod"

print(f"19: {text[-10:3]}")  # Output will be: 19: Kod
'''

print(f"20: {text[-2:5]}")

# String slicing questions on "KODNEST"

string = "KODNEST"
print(f"The String is {string}")
print(f"-------------------------------------------------")

print(f"Q1: {string[0:4]}")
print(f"Q2: {string[2:7]}")
print(f"Q3: {string[:5]}")
print(f"Q4: {string[3:]}")
print(f"Q5: {string[-4:]}")

print(f"Q6: {string[0:7:2]}")
print(f"Q7: {string[1:6:2]}")
print(f"Q8: {string[::3]}")
print(f"Q9: {string[2:7:3]}")
print(f"Q10:{string[5:7:1]}")
print(f"Q11:{string[6:0:-1]}")
print(f"Q12:{string[::-1]}")
print(f"Q13:{string[5:1:-2]}")
print(f"Q14:{string[4:0:-1]}")
print(f"Q15:{string[-1:-6:-1]}")

print(f"Q16:{string[3:5:-1]}")
# string[3:5:-1] means:
# Start at index 3 → 'N'
# End at index 5 → 'S' (but end is NOT included)
# Step = -1 → move backward (right to left)

# Problem:
# When step = -1, Python expects start > end (to move backward)
# But here start = 3 and end = 5 → start < end ❌
# So Python cannot move backward from 3 to 5

# Result:
# Empty string ("")

print(f"Q17: {string[1:5:-1]}")
print(f"Q18: {string[-2:0:-2]}")
print(f"Q19: {string[0:7:-1]}")
print(f"Q20: {string[3::-1]}")
# string[3::-1] means:
# Start at index 3 → 'N'
# End is not given → so Python goes till the beginning of the string
# Step = -1 → move backward (right to left)

# So traversal will be:
# index 3 → 'N'
# index 2 → 'D'
# index 1 → 'O'
# index 0 → 'K'

# Combine all → "NDOK"