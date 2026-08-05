lst = [1, 2, 3, 4]

# Map
def square(x):
    return x * 2
squares = list(map(square,lst))
print(squares)
# Map in lamda Function
double = list(map(lambda x: x * 2, lst))
print(double)

# Filter
def is_even(x):
    if x % 2 == 0:
        return x
even = list(filter(is_even, lst))
print(even)
# Lamda
even1 = (filter(lambda x: x % 2 == 0, lst))
print(type(even1))

# Reduce
from functools import reduce
def addup(a, b):
    return a + b
sum1 = reduce(addup, lst)
print(sum1)
# lamda
sum2 = reduce(lambda a, b: a + b, lst)
print(sum2)




