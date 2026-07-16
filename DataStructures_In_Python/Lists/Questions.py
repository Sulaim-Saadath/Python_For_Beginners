numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]

print(f"Original List: {numbers}")

# 1. First 4 Elements
print(f"First 4 elements: {numbers[:4]}") # [5, 10, 15, 20]

# 2. Last 4 Elements
print(f"Last 4 elements: {numbers[-4:]}")

# 3. Elements from index 2 to 6
print(f"Elements from index 2 to 6 {numbers[2:6]}")

# 4. Skip one element
print(f"Skip one element {numbers[::2]}")

# 5. Skip third element
print(f"Skip third element {numbers[::3]}")

# 6. Reverse entire list
print(f"Reverse entire list {numbers[::-1]}")

# 7. Elements except first two
print(f"Elements except first two: {numbers[2:]}")

# 8. Elements except last two
print(f"Elements except last two {numbers[:len(numbers) - 2]}")

# 9. Reverse a portion
print(f"Reverse a portion: {numbers[7:3:-1]}")

# 10. Copy List
copyList = numbers.copy()
print(f"Copy List: {copyList}")

# 11. Middle Elements
print(f"Middle Elements: {numbers[3:6]}")

# 12. Odd Index Elements
print(f"Odd Index Elements {numbers[1::2]}")

# 13. Even Index Elements
print(f"Even Index Elements {numbers[0::2]}")
