name = "Sulaim"
age = 20

# Pyhton is dynamically typed programming language as we need not to specify data type

# To give same value to different variables we declare and initalise like this 
a = b = c = "Saadath"
print(a, b, c)

# To give three different values in three different variables
e, f, g = 10, 20, 30
print(e, f, g)

firstName = "sulaim"
firstName = 20
print(firstName) # The 20 value is printted as python is dynamically typed the value which is assigned latest in run time that value is assigned to the variable

# Python is case sensitive
a = 10
A = 5
print(A)

# Calculating area of rectangle
length = 5
width = 10
area = length * width
print("Area of Rectangle: ",area)

print("The area of rectangle is " + str(area) + " the length is " + str(length) + " and the width is: " + str(width)) # Complex

print(f"The area of rectangle is {area} of length {length} and width {width}")