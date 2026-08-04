# @decorator name
def decor(func):
    def wrapper(name):
        if name == "Sulaim":
            print(f"{name}, Likes Shawarma.")
        else:
            print(f"{name}, Likes Biryani") 
    return wrapper         
    pass

@decor
def process(name):
    print(f"{name}, Likes Biryani")
process("Saadath")
process("Sulaim") # Sulaim likes Shawarma (Without modfying the original function)
process("Avoor")
process("DL")

print("---------------Example---------------")
# Decorator function
def smartdiv(function):
    def inner(a, b):
        if b == 0:
            print(f"Division by {b} is not possible.")
        else:
            print(a/b)
    return inner
# original function
a = int(input())
b = int(input())
@smartdiv
def div(a, b):
    print(a/b)
    pass
div(a,b)

print("---------------Decorater with arguments---------------")
# Step 1: Define a decorator that takes an argument

def repeat(num_times):
    def decorator(func):
        def wrapper():
            for _ in range(num_times):
                func()
        return wrapper
    return decorator


# Step 2: Apply the decorator with an argument

@repeat(num_times=3)
def greet():
    print("Hello!")


# Step 3: Call the decorated function

greet()