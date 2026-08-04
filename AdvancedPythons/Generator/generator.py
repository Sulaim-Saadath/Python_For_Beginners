# Generator Function
def gen_f():
    yield 1
    yield 2
    yield 3
gen = gen_f()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) (Stop Iterator Excption)

# Normal Function
def normal():
    return [2,4,6]
print(normal())