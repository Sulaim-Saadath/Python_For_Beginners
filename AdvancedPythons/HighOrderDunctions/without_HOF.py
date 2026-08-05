def mulwith2(lst):
    list1 =  []
    for n in lst:
        list1.append(n * 2)
    return list1
def even(lst):
    list1 = []
    for n in lst:
        if n % 2 == 0:
            list1.append(n)
    return list1
def summoflst(lst):
    sum = 0
    for n in lst:
        sum = sum + n
    return sum
num = input().split()
lst = []
for n in num:
    lst.append(int(n))
print("New List", mulwith2(lst))
print("Even numbers in list",even(lst))
print("Sum of elements in list",summoflst(lst))