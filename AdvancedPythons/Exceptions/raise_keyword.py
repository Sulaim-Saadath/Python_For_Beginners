# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#        raise ValueError("Age is negative")
#     print(f"Your age is {age}")
# except Exception as e:
#     print(e)

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate root of a negative number")
    return number ** 0.5
try:
    result = calculate_square_root(-9)
    print(f"The result is: {result}")
except ValueError as e:
    print(f"Error: {e}")
