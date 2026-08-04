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