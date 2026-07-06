# For loop
# 0 1 2 3 4 

for i in range(0,5):
    print(f"Iteration: {i}")

# Print n even numbers
num = int(input())
for i in range(num):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        continue