# 1. Squares of numbers
sqr = [6,5,3,1,7]
new_sqr = []
for n in sqr:
    new_sqr.append(n * n)
print("Original List:",sqr)
print("Square of the list is",new_sqr)

# Output
# Original List: [6, 5, 3, 1, 7]
# Square of the list is [36, 25, 9, 1, 49]

# 2. Odd Numbers only
odd_numbers = []
for n in sqr:
    if n % 2 != 0:
        odd_numbers.append(n)
    pass
print("Odd Numbers:",odd_numbers)

# Output
# Odd Numbers: [5, 3, 1, 7]

# 3. Convert Strings to UpperCase
names = ["ram", "sam", "john"]
upper_names = []
for n in names:
    upper_names.append(n.upper())
print("Original list:",names)
print("UpperCase List:",upper_names)

# Output
# Original list: ['ram', 'sam', 'john']
# UpperCase List: ['RAM', 'SAM', 'JOHN']

# 4. Numbers greater than 10
numbers = [6,3,19,16,2]
new_numbers = []
for n in numbers:
    if n > 10:
        new_numbers.append(n)
    pass
print("Original List:",numbers)
print("Numbers Greater than 10:",new_numbers)

# Output
# Original List: [6, 3, 19, 16, 2]
# Numbers Greater than 10: [19, 16]

# 5. Negative numbers are replaced with zero
integers = [9, -7, 5, -2, -4, 5]
wholeNumbers = []
for n in integers:
    if n < 0:
        wholeNumbers.append(0)
    else: 
        wholeNumbers.append(n)
print("Original Numbers:",integers)
print("Whole Numbers:",wholeNumbers)

# Output
# Original Numbers: [9, -7, 5, -2, -4, 5]
# Whole Numbers: [9, 0, 5, 0, 0, 5]
    
