# print("------------------------NORMAL FUNCTION---------------------------------")
# def count_num(n):
#     numbers = []
#     count = 1
#     while count <= n:
#         numbers.append(count)
#         count += 1
#     return numbers

# num = int(input("Enter the count: "))
# for n in count_num(num):
#     print(n)
print("------------------------GENERATOR FUNCTION---------------------------------")
def count_num(n):
    count = 1
    while count <= n:
        yield count
        count += 1
n = int(input("Enter the num: "))
for num in count_num(n):
    print(num)